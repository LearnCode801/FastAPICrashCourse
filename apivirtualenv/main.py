from fastapi import FastAPI ,Response, HTTPException,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
import time
from . import models
from .database import engin

models.Base.metadata.create_all(bind=engin)
app=FastAPI()

class Post(BaseModel):
    id :  int
    title :str
    content :str
    publish : bool =True
    rating : Optional[float] = None




try:
    conn=psycopg2.connect(host='localhost',
                          database="fastapi",
                          user='postgres',
                          password='1234')
    cursor=conn.cursor()
    print("\nDatabase conected sucessfully")

except Exception as error:
    print('\nConnecting data base iss failed')   
    print(error) 
    time.sleep(2)


my_posts_list=[
    {
    'id':'1',
    'title':'first title',
    'content': 'this us the first content'
    }
]
def get_one_post_with_id(id : int):
    for p in my_posts_list:
        if int(p['id'])==id:
            return p
        else :
            continue

    return None
 

def delete_post_with_id(id:id):
    for i, post in enumerate(my_posts_list):
        if int(post['id'])==id:
            my_posts_list.pop(i)
            return True
        else :
            continue

    return False
     

def update_post_with_id(id :id, post: Post):
    mypost_dict=post.dict()
    mypost_dict['id']=id
    my_posts_list[id]=mypost_dict

    return True


@app.get('/')
def view_all_post():
    return my_posts_list

@app.post('/post',status_code=status.HTTP_201_CREATED)
def post_the_new_post(new_post: Post ):
    print('\n==========================')
    my_posts_list.append(new_post.dict())
    print('==========================')
    return {
        'massage':f'Successfully added the post with id{new_post.id}'
    }

@app.get('/get_single_post/{id}')
def get_single_post(id:int):
    id=int(id)
    retrived_one_post=get_one_post_with_id(id)
    if retrived_one_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id}')
        
    return {
        f'post of {id}':retrived_one_post
    }


@app.delete('/delete_post/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_the_single_post(id:int):
    deleted_post=delete_post_with_id(id)

    if deleted_post == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id : {id}')
        
    return {
       Response(status_code=status.HTTP_204_NO_CONTENT)
    }

@app.put('/update_post/{id}')
def update_post(id:int, post : Post):

    updated_post=update_post_with_id(id,post)

    if updated_post == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the updatating index : {id}')
    
    return {
        'message':'successfully updated'
    }






@app.post('/create_post1')
def create_post1(pyload :dict = Body(...)):
    print("\n========================")
    print(pyload)
    print("========================\n")
    return {'created post':f"{pyload}"}

@app.post('/create_post2')
def create_post2(new_post : Post):

    print("\n========================")
    print(new_post)
    print("========================\n")
    print(new_post.title)
    print(new_post.content)
    print("========================\n")
    return {
                "new  .. post":new_post
            }


