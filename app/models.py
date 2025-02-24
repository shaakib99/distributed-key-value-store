from pydantic import BaseModel
from typing import Optional

class AppDataModel(BaseModel):
    id: str = None
    name: str = None
    description: str = None
    created_at: str = None
    updated_at: str = None

class CreateAppDataModel(BaseModel):
    name: str
    description: str

class UpdateAppDataModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class AppDataResponseModel(BaseModel):
    id: str | int
    name: str
    description: str | None
    created_at: str
    updated_at: str