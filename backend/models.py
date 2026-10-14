from __future__ import annotations
from datetime import datetime
from sqlalchemy import DateTime, Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from backend.db import Base
def utcnow(): return datetime.utcnow()
class PriceQuote(Base):
    __tablename__ = "price_quotes"
    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    package: Mapped[str] = mapped_column(String(80))
    features: Mapped[str] = mapped_column(Text)
    anchor: Mapped[float] = mapped_column(Float, default=0.0)
    suggested: Mapped[float] = mapped_column(Float, default=0.0)
    rationale: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow)
