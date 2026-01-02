from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.utils.init_db import create_table
from app.routers.auth import authRouter
from app.db.schema.user import UserOutput
from app.utils.protectRoute import get_current_user

# lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Created")
    create_table()
    yield
    

app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter, tags=["auth"], prefix="/auth")

@app.get("/health")
def health_check():
    return {
        "status":"Running"
    }
    
@app.get("/protected")
def read_protected(user : UserOutput = Depends(get_current_user)):
    return {"data":user}