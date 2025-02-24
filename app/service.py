from database_service.service import DatabaseService
from pydantic import BaseModel
from app.schema import AppDataSchema
from app.models import CreateAppDataModel, AppDataModel, UpdateAppDataModel
from datetime import datetime

class AppService:
    def __init__(self, database_service: DatabaseService = None):
        self.database_service = database_service or DatabaseService(AppDataSchema, None)

    async def get_one(self, id: str):
        return await self.database_service.get_one(id)
    
    async def get_all(self, query: BaseModel):
        return await self.database_service.get_all(query)
    
    async def create_one(self, data: CreateAppDataModel):
        appDataModel = AppDataModel()
        appDataModel.name = data.name
        appDataModel.description = data.description
        appDataModel.created_at = datetime.now() 
        appDataModel.updated_at = datetime.now()
        return await self.database_service.create_one(appDataModel)

    async def update_one(self, id: str, data: UpdateAppDataModel):
        return await self.database_service.update_one(id, data)

    async def delete_one(self, id: str):
        return await self.database_service.delete_one(id)