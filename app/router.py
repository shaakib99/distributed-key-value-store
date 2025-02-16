from fastapi import APIRouter
from app.service import AppService

router = APIRouter(prefix="/app", tags=["app"])

app_service = AppService()

@router.get("{id}")
async def get_one(id: str):
    return app_service.get_one(id)

@router.post("")
async def create_one(data: dict):
    return app_service.create_one(data)

@router.put("{id}")
async def update_one(id, data: dict):
    return app_service.update_one(id, data)

