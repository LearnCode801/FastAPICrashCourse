from fastapi import FastAPI ,Response, HTTPException,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
import time

class Post(BaseModel):
    # id :  int
    title :str
    content :str
    published : bool =True
    # rating : Optional[float] = None


app=FastAPI()

while True:
    try:
        conn=psycopg2.connect(host='localhost',
                          database="fastapi",
                          user='postgres',
                          password='1234')
        cursor=conn.cursor()
        print("\nDatabase conected sucessfully")
        break

    except Exception as error:
        print('\nConnecting data base iss failed')   
        print(error) 
        time.sleep(2)
@app.get('/')
def wellcomepoint():
    return{
        'hi':'wellcome to fastapi'
    }
@app.get('/get_all_post_posts')
def get_all_post():
    cursor.execute("""SELECT * FROM postblog """)
    all_posts=cursor.fetchall()
    return {
        'all_post':all_posts
    }

@app.get('/get_single_post_by_id/{id}')
def get_single_post_by_id(id :int):
    cursor.execute(''' select * from postblog where id = %s ''',(str(id)))
    posts=cursor.fetchall()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id}')
    
    return {
        'all_post':posts
    }

@app.post('/post_new_post', status_code=status.HTTP_201_CREATED)
def post_new_post(new_post: Post):
    print(new_post)
    cursor.execute('''insert into postblog (title,content,published) 
                   values (%s, %s, %s) returning * ''',
                   (new_post.title, new_post.content, new_post.published) )
    added_post=cursor.fetchone()
    conn.commit()
    return{
        'added_post':added_post
    }

@app.delete('/delete_onepost_by_id/{id}', status_code=status.HTTP_404_NOT_FOUND)
def delete_onepost_by_id(id :int ):
    cursor.execute('''delete from postblog where id = %s returning * ''',(str(id)))
    deleted_post=cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id} for deletion')
    
    return {
        'deleted_post':deleted_post
    }

@app.put('/update_post/{id}')
def update_post(id :int, post:Post):

    cursor.execute('''update postblog  set title =%s, content=%s, published = %s where id = %s returning * ''',(post.title,post.content,post.published,str(id)))
    updated_post=cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Could notupdate/notexist the posts with the id  {id}')
    
    return {
        'deleted_post':updated_post
    }
    