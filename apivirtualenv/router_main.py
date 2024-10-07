from fastapi import FastAPI
from  .database import engin
from . import models
from .routers import post, user, auth ,vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engin)

app=FastAPI()
# origins=[
#     "https://www.google.com",
#     "https://www.youtube.com"
# ]
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def wellcomepoint():
    return{
        'hi':'wellcome to fastapi CRUD with ORM Sqlalchemy'
    }

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)




    


    