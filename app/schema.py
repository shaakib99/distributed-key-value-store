from sqlalchemy import Column, Integer, String
from database_service.mysql_database import Base

class AppDataSchema(Base):
    __tablename__ = "app_data"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    created_at = Column(String(255))
    updated_at = Column(String(255))