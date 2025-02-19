from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from app.router import router as AppRouter
from database_service.database_metadata_manager import DatabaseMetadataManager

async def lifespan(app):
    load_dotenv()
    DatabaseMetadataManager().create_tables()
    yield

app = FastAPI(lifespan=lifespan)

routers: list[APIRouter] = [AppRouter]
for router in routers:
    app.include_router(router)
