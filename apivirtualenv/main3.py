from fastapi import FastAPI ,Response, HTTPException,status,Depends
from fastapi.params import Body
from pydantic import BaseModel

from typing import Optional  , List
import psycopg2
import time
from  .database import engin, get_db
from . import models ,schemas ,utils
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engin)

app=FastAPI()



@app.get('/')
def wellcomepoint():
    return{
        'hi':'wellcome to fastapi CRUD with ORM Sqlalchemy'
    }

@app.get('/get_all_post_posts', response_model=List[schemas.PostResponce])
def get_all_post(db: Session=Depends(get_db)):
    post=db.query(models.Post).all()

    return post



@app.get('/get_single_post_by_id/{id}', response_model=schemas.PostResponce)
def get_single_post_by_id(id :int, db: Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id == id ).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id}')
    
    return post





@app.post('/post_new_post', status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponce)
def post_new_post(post: schemas.PostCreated, db: Session=Depends(get_db)):
    new_post=models.Post(
        **post.dict())
    # new_post=models.Post(
    #     title=post.title, 
    #     content=post.content, 
    #     published=post.published )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
    


@app.delete('/delete_onepost_by_id/{id}', status_code=status.HTTP_404_NOT_FOUND)
def delete_onepost_by_id(id :int ,db: Session=Depends(get_db) ):
    delete_post=db.query(models.Post).filter(models.Post.id == id)
    if delete_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id} for deletion')
    
    delete_post.delete(synchronize_session=False)
    db.commit()



@app.put('/update_post/{id}', response_model=schemas.PostResponce)
def update_post(id :int ,update_post:schemas.PostUpdate, db: Session=Depends(get_db)):
    
    post_qurey=db.query(models.Post).filter(models.Post.id==id)

    post=post_qurey.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id} for deletion')
    
    post_qurey.update(update_post.dict(), synchronize_session=False)
    db.commit()

    return post_qurey.first()
    
@app.post('/registerUser', status_code=status.HTTP_201_CREATED,response_model =schemas.UserCreateResponce)
def registerUser(user: schemas.UserCreate, db: Session=Depends(get_db)):
    
    hashed_password= utils.hash_password(user.password)
    user.password=hashed_password

    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get('/get_info_of_single_user_by_id/{id}', response_model=schemas.UserCreateResponce)
def get_info_of_single_user_by_id(id:int, db: Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the User with the id {id}')
    
    return user

    