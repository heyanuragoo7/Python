from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models import User
import os

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/fastapi_db")

client = AsyncIOMotorClient(MONGODB_URL)
database = client.fastapi_db

# Initialize Beanie with the database
async def init_db():
    await init_beanie(database=database, document_models=[User])

# Dependency to get database
def get_database():
    return database