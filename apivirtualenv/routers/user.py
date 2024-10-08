from fastapi import  HTTPException,status,Depends ,APIRouter
from  ..database import  get_db
from .. import models ,schemas ,utils
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/registerUser', status_code=status.HTTP_201_CREATED,response_model =schemas.UserCreateResponce)
def registerUser(user: schemas.UserCreate, db: Session=Depends(get_db)):
    
    hashed_password= utils.hash_password(user.password)
    user.password=hashed_password

    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/get_info_of_single_user_by_id/{id}', response_model=schemas.UserCreateResponce)
def get_info_of_single_user_by_id(id:int, db: Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the User with the id {id}')
    
    return user