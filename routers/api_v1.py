from fastapi import APIRouter
from routers import auth_router, responsible_router, therapist_router

router = APIRouter(prefix="/api/v1")

router.include_router(auth_router.router, tags=["Autenticação"])
router.include_router(therapist_router, tags=["Terapeutas"])
router.include_router(responsible_router, tags=["Responsáveis"])