from database_service.database_metadata_manager import DatabaseMetadataManager

class DatabaseService:
    def __init__(self, schema, database_metadata_manager):
        self.schema = schema
        self.database_metadata_manager = database_metadata_manager or DatabaseMetadataManager()

    async def create_one(self, data: dict):
        key = self.database_metadata_manager.get_key()
        database = self.database_metadata_manager.get_db(key)
        print(database)
        return {"message": "Hello World from database"}
    
    async def get_one(self, id: str):
        database = self.database_metadata_manager.get_db(id)
        print(database)
        return {"message": f"Hello World from database {id}"}
    
    async def get_all(self):
        return {"message": "Hello World from database"}
    
    async def update_one(self, id: str, data: dict):
        database = self.database_metadata_manager.get_db(id)
        print(database)
        return {"message": f"Hello World from database {id}"}
    
    async def delete_one(self, id: str):
        database = self.database_metadata_manager.get_db(id)
        print(database)
        return {"message": f"Hello World from database {id}"}
    