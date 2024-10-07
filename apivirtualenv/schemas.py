from pydantic import BaseModel ,EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title :str
    content :str
    published : bool =True

class PostCreated(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class UserCreateResponce(BaseModel):
    id : int
    email:EmailStr
    created_at : datetime 
    class Config:
        orm_mode=True

class PostResponce(PostBase):
    id : int
    created_at : datetime
    owner_id: int
    owner: UserCreateResponce
    class Config:
        orm_mode=True

class PostvoteResponce(BaseModel):
    Post:PostResponce
    vote:int
    



class UserCreate(BaseModel):
    name: str
    email:EmailStr
    password:str


class UserLogin(BaseModel):
    email :EmailStr
    password :str        

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id:int
    dir_ :bool