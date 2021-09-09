from os import name
from fastapi import FastAPI,HTTPException,status,Response,Request
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.sqltypes import Integer
from starlette import responses
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
import logging,json
from pydantic import ValidationError
from fastapi.responses import JSONResponse,PlainTextResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError,RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

import logging
app=FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     logging.basicConfig(filename="test.log",level=logging.INFO,format='%(asctime)s  :  %(levelname)s : %(message)s')
    

models.Base.metadata.create_all(engine)

app = FastAPI()

# @app.exception_handler(RequestValidationError)
# @app.exception_handler(ValidationError)
# async def validation_exception_handler(request, exc):
#     content=jsonable_encoder({"detail":exc.errors()})
#     detail=content['detail']
#     loc=detail[0]
#     container=loc['loc'][1]
#     msg=loc['msg']
#     return JSONResponse(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         content=jsonable_encoder({
#             "error": {container:msg} ,
#         }),
#     )


# async def catch_exceptions_middleware(request: Request, call_next):
#     try:
#         return await call_next(request)
#     except Exception as exc:
        
#         return JSONResponse(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             content=jsonable_encoder({"error": exc.args}),
#         )
# app.middleware('http')(catch_exceptions_middleware)




def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/")
async def create_item(item: schemas.Item):
    # a=3/0 
    # a=b+2 
    
    return item


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
def featured_products(db:Session=Depends(get_db)):
    products=db.query(models.Products).all()
    return products


# API to search products 
@app.get('/product/{name}')
def search_products(name:str ,db:Session=Depends(get_db) ):
    products=db.query(models.Products).filter(models.Products.name==name).all()
    return products




# Api to give details of each product by id
@app.get('/product/{id}/')
async def search_products(id:int ,db:Session=Depends(get_db) ):
    products=db.query(models.Products).filter(models.Products.id==id).all()
   
    return products

# return {"item_id": item_id, **item.dict()}
    


# API to register user
@app.post('/user')
def register_user(request:schemas.User,db:Session=Depends(get_db)):
    new_user=models.User(first_name=request.first_name,last_name=request.last_name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# API to login user
@app.post('/login')
def login(request:schemas.Login,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.email,models.User.password==request.password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No user found")
    return user
    

    

# API for profile update of user
@app.put('/profile/{id}')
def profile_update(id:int,request:schemas.User,db:Session=Depends(get_db)):
    db.query(models.User).filter(models.User.id==id).update(request.dict())
    db.commit()
    return request





 
    # except ValidationError as exc: 
        
    #     return  JSONResponse(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         content=jsonable_encoder({"detail": exc.errors()}),
    #     )
