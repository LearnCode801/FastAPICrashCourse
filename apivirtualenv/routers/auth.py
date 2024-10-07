from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import database, schemas,models,utils, oauth2
router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(user_cardentials : OAuth2PasswordRequestForm=Depends(),  db: Session=Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_cardentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Cardentials")
    
    if not utils.varify(user_cardentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Cardentials")
    
    access_token=oauth2.create_access_token(data={'user_id':user.id})
    return{
        'access_token':access_token,
        'token_type':'barrer**********rrrr'
    }













# @router.post('/login')
# def login(user_cardentials : schemas.UserLogin,  db: Session=Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email == user_cardentials.email).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"Invalid Cardentials")
    
#     if not utils.varify(user_cardentials.password,user.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"Invalid Cardentials")
    
#     access_token=oauth2.create_access_token(data={'user_id':user.id})
#     return{
#         'access_token':access_token,
#         'token_type':'barrer'
#     }
    