from app.core.database import Base
from sqlalchemy import Column, Integer, Float, String

class User(Base):

    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String, unique=True)
    password = Column(String(250))