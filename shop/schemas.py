import logging
from pydantic import BaseModel,validator
from typing import Optional
from . import main

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
    
    

class Item(BaseModel):
    title: str
    size: int