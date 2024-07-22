from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=50), unique=True, index=True)
    email = Column(String(length=100), unique=True, index=True)
    password_hash = Column(String(length=255))
    name = Column(String(length=100))
    preferences = Column(JSON)
