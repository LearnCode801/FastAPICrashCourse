from fastapi import  HTTPException,status,Depends ,APIRouter
from typing import  List
from  ..database import  get_db
from .. import models ,schemas ,oauth2
from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy import func

router = APIRouter(
    prefix="/post",
    tags=['Posts']
)


@router.get('/get_all_post')
def get_all_post(db: Session=Depends(get_db), current_user:int = Depends(oauth2.get_current_user),
                 limit:int = 3, skip:int =1, search:Optional[str]="" ):

    posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip)
    # http://127.0.0.1:8000/post/get_all_post?limit=2&skip=0&search=updated%20title

    result=db.query(models.Post, func.count(models.Vote.post_id).label("votes") ).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)
    
    # ---------------------------------(  joinging with the filters  )-------------------------------------------
    res=db.query(models.Post, func.count(models.Vote.post_id).label("votes") ).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
            models.Post.title.contains(search)).limit(limit).offset(skip)
    # -----------------------------------------------------------------------------------------------------------
    
    print("\n#############################################################################")
    print(posts)
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(result)
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(res)
    print("\n############################################################################")
    return posts.all()


# @router.get('/get_all_post', response_model=List[schemas.PostResponce])
# def get_all_post(db: Session=Depends(get_db), current_user:int = Depends(oauth2.get_current_user),
#                  limit:int = 3, skip:int =1, search:Optional[str]="" ):

#     posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
#     # http://127.0.0.1:8000/post/get_all_post?limit=2&skip=0&search=updated%20title

#     return posts



@router.get('/get_single_post_by_id/{id}', response_model=schemas.PostResponce)
def get_single_post_by_id(id :int, db: Session=Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    
    post=db.query(models.Post).filter(models.Post.id == id ).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id}')
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                      detail=f'Not Authorized to perform request action')
    
    return post





@router.post('/post_new_post', status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponce)
def post_new_post(post: schemas.PostCreated, db: Session=Depends(get_db), 
                  current_user:int = Depends(oauth2.get_current_user)):
     
    new_post=models.Post(owner_id=current_user.id,**post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
    


@router.delete('/delete_onepost_by_id/{id}', status_code=status.HTTP_404_NOT_FOUND)
def delete_onepost_by_id(id :int ,db: Session=Depends(get_db), current_user:int = Depends(oauth2.get_current_user) ):

    delete_query=db.query(models.Post).filter(models.Post.id == id)
    delete_post=delete_query.first()

    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id} for deletion')
    
    print("\n*********current_user**********")
    print(current_user.id)
    print("\n*******************")
    
    if delete_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                      detail=f'Not Authorized to perform request action')
    

    delete_query.delete(synchronize_session=False)
    db.commit()



@router.put('/update_post/{id}', response_model=schemas.PostResponce)
def update_post(id :int ,update_post:schemas.PostUpdate, db: Session=Depends(get_db), 
                current_user:int = Depends(oauth2.get_current_user)):
    
    update_qurey=db.query(models.Post).filter(models.Post.id==id)

    post=update_qurey.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Not found the post with the id {id} for deletion')
    
    print("\n*********current_user**********")
    print(current_user)
    print("\n*******************")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                      detail=f'Not Authorized to ========== perform request action')
    
    update_qurey.update(update_post.dict(), synchronize_session=False)
    db.commit()

    return update_qurey.first()
