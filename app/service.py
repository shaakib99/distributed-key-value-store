class AppService:
    def __init__(self):
        pass

    async def get_one(self, id: str):
        return {"message": f"Hello World from app {id}"}
    
    async def create_one(self, data: dict):
        return {"message": "Hello World from app"}

    async def update_one(self, id: str, data):
        return {"message": f"Hello World from app {id}"}
