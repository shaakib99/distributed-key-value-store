from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
class MySQLDatabase:
    instance = None

    def __init__(self):
        host = os.getenv("MYSQL_HOST")
        self.engine = create_engine(host)
        self.session = sessionmaker(bind=self.engine)()
        self.base = declarative_base()
        self.base.metadata.create_all(self.engine)

    def get_instance():
        if MySQLDatabase.instance is None:
            MySQLDatabase.instance = MySQLDatabase()
        return MySQLDatabase.instance

    async def create_one(self, data: dict, schema):
        return {"message": "Hello World from MySQL database"}
    
    async def get_one(self, id: str, schema):
        return {"message": f"Hello World from MySQL database {id}"} 
    
    async def get_all(self, schema):
        return {"message": "Hello World from MySQL database"}  
    
    async def update_one(self, id: str, data: dict, schema):    
        return {"message": f"Hello World from MySQL database {id}"}
    
    async def delete_one(self, id: str, schema):
        return {"message": f"Hello World from MySQL database {id}"}