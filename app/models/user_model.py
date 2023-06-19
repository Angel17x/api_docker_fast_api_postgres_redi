from pydantic import BaseModel;
from typing import Optional;

class UserModel(BaseModel):
    user_id: Optional[str]
    name: str
    lastname: str
    age: Optional[str]
    email: str
    password: Optional[str] = None
    user_type: Optional[str]
    
    class Config:
        orm_mode = True
        fields = {
            "password": {"exclude": True}
        }
