from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db import get_db
from backend.services import pricing as svc

class QuoteIn(BaseModel):
    package: str = Field(min_length=2)
    features: str = Field(min_length=3)
    anchor: float = 0

router = APIRouter()

@router.get("/quotes")
async def quotes(db: AsyncSession = Depends(get_db)):
    rows = await svc.list_quotes(db)
    return {"quotes": [{"id": q.id, "package": q.package, "suggested": q.suggested, "anchor": q.anchor, "rationale": q.rationale[:280]} for q in rows]}

@router.post("/quotes")
async def create(payload: QuoteIn, db: AsyncSession = Depends(get_db)):
    q = await svc.suggest(db, payload.package, payload.features, payload.anchor)
    return {"id": q.id, "suggested": q.suggested}
