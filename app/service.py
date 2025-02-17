from database_service.service import DatabaseService
class AppService:
    def __init__(self, database_service: DatabaseService = None):
        self.database_service = database_service or DatabaseService(None, None)

    async def get_one(self, id: str):
        return self.database_service.get_one(id)
    
    async def create_one(self, data: dict):
        return self.database_service.create_one(data)

    async def update_one(self, id: str, data):
        return self.database_service.update_one(id, data)
