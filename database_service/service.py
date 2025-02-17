from database_service.mysql_database import MySQLDatabase

class DatabaseService:
    def __init__(self, schema, database):
        self.schema = schema
        self.database = database or MySQLDatabase.get_instance()

    async def create_one(self, data: dict):
        return {"message": "Hello World from database"}
    
    async def get_one(self, id: str):
        return {"message": f"Hello World from database {id}"}
    
    async def get_all(self):
        return {"message": "Hello World from database"}
    
    async def update_one(self, id: str, data: dict):
        return {"message": f"Hello World from database {id}"}
    
    async def delete_one(self, id: str):
        return {"message": f"Hello World from database {id}"}
    