from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from rhh.infrastructure.api.routes import animatronics
from rhh.shared.exceptions import RavenHillHouseError

api_router = APIRouter()
api_router.include_router(animatronics.router, prefix="/props", tags=["props"])