from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables
from app.routers.auth import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    # Create database tables
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router, tags=["Authentication"], prefix="/auth")
# app.include_router(router=router, tags=["Users"], prefix='/users')

@app.get('/health')
def health():
    return {
        "message": "Healthy"
    }