from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class AppData(Base):
    __tablename__ = "app_data"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    created_at = Column(String(255))
    updated_at = Column(String(255))