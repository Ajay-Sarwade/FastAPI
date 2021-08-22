from pydantic import BaseModel

class Banner(BaseModel):
    url:str

class User(BaseModel):
    first_name:str
    last_name:str
    email:str
    password:str

class Login(User):
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