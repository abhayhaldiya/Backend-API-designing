from typing import List
from fastapi import APIRouter,Depends,status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

userid:str=Depends(oauth2.get_id)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(userid,request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(userid,request, db)

@router.delete('/{Title}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(Title:str, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(Title,db)


@router.put('/{Title}', status_code=status.HTTP_202_ACCEPTED)
def update(Title:str, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(Title,request, db)


@router.get('/{Title}', status_code=200, response_model=schemas.ShowBlog)
def show(Title:str, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(Title,db)