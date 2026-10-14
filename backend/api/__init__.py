from fastapi import APIRouter
from backend.api import health, pricing, ui
api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(pricing.router, prefix="/api", tags=["pricing"])
api_router.include_router(ui.router, tags=["ui"])
