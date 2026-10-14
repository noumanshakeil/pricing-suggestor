from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db import get_db
from backend.services import pricing as svc

router = APIRouter()
templates = Jinja2Templates(directory="backend/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, db: AsyncSession = Depends(get_db)):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Pricing Suggestor", "quotes": await svc.list_quotes(db)})

@router.post("/ui/quotes")
async def ui_q(package: str = Form(...), features: str = Form(...), anchor: float = Form(99), db: AsyncSession = Depends(get_db)):
    await svc.suggest(db, package, features, anchor); return RedirectResponse("/", status_code=303)
