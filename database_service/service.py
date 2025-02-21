from database_service.database_metadata_manager import DatabaseMetadataManager
from pydantic import BaseModel

class DatabaseService:
    def __init__(self, schema, database_metadata_manager):
        self.schema = schema
        self.database_metadata_manager = database_metadata_manager or DatabaseMetadataManager()

    async def create_one(self, data: BaseModel):
        key = self.database_metadata_manager.get_key()
        database = self.database_metadata_manager.get_db(key)
        setattr(data, "id", key)
        return await database.create_one(data, self.schema)
    
    async def get_one(self, id: str):
        database = self.database_metadata_manager.get_db(id)
        print(database.host)
        return await database.get_one(id, self.schema)
    
    async def get_all(self, query: BaseModel):
        databases = self.database_metadata_manager.get_all_db()
        result = []
        for database in databases:
            result.append(await database.get_all(query, self.schema))
        result = sorted(result, key=lambda x: x["id"])
        return result
    
    async def update_one(self, id: str, data: BaseModel):
        database = self.database_metadata_manager.get_db(id)
        return await database.update_one(id, data, self.schema)
    
    async def delete_one(self, id: str):
        database = self.database_metadata_manager.get_db(id)
        return await database.delete_one(id, self.schema)
    