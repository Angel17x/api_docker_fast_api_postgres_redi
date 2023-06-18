from pydantic import BaseModel;
from typing import Optional;

class UserModel(BaseModel):
    id: Optional[str]
    name: str
    lastname: str
    age: int
    nickname: str
    password: str
    work: str
