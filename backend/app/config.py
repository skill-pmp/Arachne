import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Point to your database
DB_PATH = os.path.join(os.path.dirname(__file__), "../../database/habits.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
