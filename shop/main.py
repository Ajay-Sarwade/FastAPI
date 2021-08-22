from os import name
from fastapi import FastAPI,HTTPException,status
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.sqltypes import Integer
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API to display all the banner urls
@app.get('/banner')
def fetch_url(db:Session=Depends(get_db)):
    banners=db.query(models.Banner).all()
    return banners


# API to create Banner
@app.post('/banner')
def create_banner(request:schemas.Banner,db:Session=Depends(get_db)):
    new_banner=models.Banner(url=request.url)
    db.add(new_banner)
    db.commit()
    db.refresh(new_banner)
    return new_banner

# API to add new product
@app.post('/product')
def add_product(request:schemas.Products,db:Session=Depends(get_db)):
    new_product=models.Products(name=request.name,url=request.url,description=request.description,price=request.price,
    size=request.size,color=request.color,review=request.review)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# API for featured product
@app.get('/product')
def featured_products(db:Session=Depends(get_db) ):
    products=db.query(models.Products).all()
    return products


# API to search products 
@app.get('/product/{name}')
async def search_products(name:str ,db:Session=Depends(get_db) ):
    products=db.query(models.Products).filter(models.Products.name==name).all()
    return products

# Api to give details of each product by id
@app.get('/product/{id}/')
async def search_products(id:int ,db:Session=Depends(get_db) ):
    products=db.query(models.Products).filter(models.Products.id==id).all()
    return products


# API to register user
@app.post('/user')
def register_user(request:schemas.User,db:Session=Depends(get_db)):
    new_user=models.User(first_name=request.first_name,last_name=request.last_name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# API to login user
@app.get('/login/{email}/{password}')
def login(email:str,password:str,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==email,models.User.password==password).first()
    if bool(user):
        return user
    return ("Register yourself")
    
    

# API for profile update of user
@app.put('/profile/{id}')
def profile_update(id:int,request:schemas.User,db:Session=Depends(get_db)):
    db.query(models.User).filter(models.User.id==id).update(request.dict())
    db.commit()
    return request





 
