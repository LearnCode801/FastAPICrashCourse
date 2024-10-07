from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import Depends, status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import schemas, database, models
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


SECRET_KEY="talha"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data:dict):
    to_encode=data.copy()

    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({'exp':expire})

    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def varify_access_token(token:str, credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        print("\n=============( payload) ==================")
        print(payload)
        print("=================================")
        id :str =payload.get("user_id")

        if id is None:
            raise credentials_exception
        print("#####################################\n")
        # token_data=schemas.TokenData(id=id)
        print("#################(TRY end)####################\n")
        # print(token_data)
        print("#################(TRY end)####################\n")

    except JWTError:
        raise credentials_exception
    
    # return token_data
    return id
    

def get_current_user(token :str = Depends(oauth2_scheme), db: Session=Depends(database.get_db)):

    credentials_exception =HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                         detail=f"Could not validate *** credential/ OR Token Expire ",
                                         headers={"WWW-Authenticate":"Bearer"}) 
    
    token=varify_access_token(token, credentials_exception) 
    user=db.query(models.User).filter(models.User.id == token).first()
    return user  