from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:2580@localhost:5432/FastApi"
engine = create_engine(db_url)
Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)