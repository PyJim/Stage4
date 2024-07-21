from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, example="John Doe")
    email: Optional[EmailStr] = Field(None, example="johndoe@example.com")
    preferences: Optional[Dict[str, bool]] = Field(None, example={"newsletter": True, "darkMode": False})

    class Config:
        orm_mode = True
        from_attributes = True 

class ResponseModel(BaseModel):
    message: str
    user: UserUpdate
    status: int
