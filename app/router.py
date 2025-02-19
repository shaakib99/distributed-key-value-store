from fastapi import APIRouter
from app.service import AppService

router = APIRouter(prefix="/app", tags=["app"])

app_service = AppService()

@router.get('/{id}')
async def get_one(id: str):
    return await app_service.get_one(id)

@router.get("/")
async def get_all():
    return app_service.get_all()

@router.post("")
async def create_one(data: dict):
    return app_service.create_one(data)

@router.put("/{id}")
async def update_one(id, data: dict):
    return app_service.update_one(id, data)

@router.delete("/{id}")
async def delete_one(id: str):
    return app_service.delete_one(id)

