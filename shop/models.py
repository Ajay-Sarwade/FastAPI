from sqlalchemy import Column,Integer,String
from sqlalchemy.sql.expression import column
from .database import Base

class Banner(Base):
    __tablename__="banner"
    id=Column(Integer,primary_key=True,index=True)
    url=Column(String)
    

class User(Base): 
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String)
    password=Column(String)

class Products(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True,index=True)
    url=Column(String)
    name=Column(String)
    description=Column(String)
    price=Column(String)
    size=Column(String)
    color=Column(String)
    review=Column(Integer)