from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from common.exceptions import NotFoundException

Base = declarative_base()

class MySQLDatabase:
    instance = {}

    def __init__(self, host: str):
        self.engine = create_engine(host)
        self.session = sessionmaker(bind=self.engine)()
        self.host = host
    
    @staticmethod
    def get_instance(host: str) -> "MySQLDatabase":
        try:
            if host not in MySQLDatabase.instance:
                connection = MySQLDatabase(host)
                connection.engine.connect()
                MySQLDatabase.instance[host] = connection
            return MySQLDatabase.instance[host]
        except Exception as e:
            raise Exception(f"Database connection error: {host}")


    async def create_one(self, data: BaseModel, schema: DeclarativeBase):
        self.session.add(schema(**data.model_dump()))
        self.session.commit()
        return data
    
    async def get_one(self, id: str, schema: DeclarativeBase):
        data = self.session.query(schema).filter(schema.id == id).first()
        if data is None:
            raise NotFoundException(f"Data with id {id} not found")
        return data
    
    async def get_all(self, query: BaseModel, schema: DeclarativeBase):
        return {"message": "Hello World from MySQL database"}  
    
    async def update_one(self, id: str, data: BaseModel, schema: DeclarativeBase):
        data = self.get_one(id, schema)
        for key, value in data.model_dump().items():
                setattr(data, key, value)
        self.session.commit()
        return data             
    
    async def delete_one(self, id: str, schema: DeclarativeBase):
        data = self.get_one(id, schema)
        self.session.delete(data)
        self.session.commit()
        return None