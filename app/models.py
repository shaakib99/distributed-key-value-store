from pydantic import BaseModel

class AppDataModel(BaseModel):
    id: str
    name: str
    description: str
    created_at: str
    updated_at: str