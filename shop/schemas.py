from pydantic import BaseModel
from typing import Optional
class Banner(BaseModel):
    url:str

class User(BaseModel):
    first_name:str
    last_name:str
    email:str
    password:str

class Login(BaseModel):
    email:str
    password:str
    class Config():
        orm_mode=True

class Products(BaseModel):
    name:str
    url:str
    description:str
    price:str
    size:str
    color:str
    review:int

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None