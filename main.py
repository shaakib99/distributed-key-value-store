from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from app.router import router as AppRouter

async def lifespan(app, event):
    load_dotenv()
    yield

app = FastAPI(lifespan=lifespan)

routers: list[APIRouter] = [AppRouter]
for router in routers:
    app.include_router(router)
