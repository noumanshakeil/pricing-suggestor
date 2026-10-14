from __future__ import annotations
import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.llm import get_llm
from backend.models import PriceQuote

async def suggest(session: AsyncSession, package: str, features: str, anchor: float = 0.0) -> PriceQuote:
    feature_count = max(1, len([f for f in features.replace(",", "\n").splitlines() if f.strip()]))
    base = anchor if anchor > 0 else 49.0
    suggested = round(base * (1.0 + 0.08 * feature_count), 2)
    llm = get_llm()
    rationale = await llm.complete(
        f"Justify price ${suggested} for package {package} with features: {features}. Anchor={anchor}",
        system="Pricing strategist. Be concrete.",
    )
    row = PriceQuote(id=uuid.uuid4().hex[:10], package=package[:80], features=features, anchor=float(anchor),
                     suggested=suggested, rationale=rationale)
    session.add(row); await session.commit(); await session.refresh(row); return row

async def list_quotes(session: AsyncSession) -> list[PriceQuote]:
    return list((await session.execute(select(PriceQuote).order_by(PriceQuote.created_at.desc()))).scalars())
