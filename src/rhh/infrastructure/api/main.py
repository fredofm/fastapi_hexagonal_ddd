from fastapi import APIRouter

from rhh.infrastructure.api.routes import animatronics

api_router = APIRouter()
api_router.include_router(animatronics.router, prefix="/props", tags=["props"])