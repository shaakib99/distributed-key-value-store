from fastapi import APIRouter
from app.service import AppService
from app.models import CreateAppDataModel, UpdateAppDataModel, AppDataResponseModel

router = APIRouter(prefix="/app", tags=["app"])

app_service = AppService()

@router.get('/{id}', response_model=AppDataResponseModel)
async def get_one(id: str):
    return await app_service.get_one(id)

@router.get("/")
async def get_all():
    return await app_service.get_all({})

@router.post("")
async def create_one(data: CreateAppDataModel):
    return await app_service.create_one(data)

@router.put("/{id}", response_model=AppDataResponseModel)
async def update_one(id: str, data: UpdateAppDataModel):
    return await app_service.update_one(id, data)

@router.delete("/{id}")
async def delete_one(id: str):
    return await app_service.delete_one(id)

