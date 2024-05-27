from fastapi import HTTPException,status,Response
from sqlalchemy.orm import Session
from ..import models,schemas
from ..database import get_db


def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(userid,request: schemas.Blog,db:Session):
    new_blog=models.Blog(title=request.title, body=request.body,user_id=userid)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(Title:str,response:Response, db:Session):
    blog=db.query(models.Blog).filter(models.Blog.title==Title).first()
    if not blog:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the title {Title} is not available')
    return blog

def update(Title:str,request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.title==Title)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with title {Title} not found")
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return blog

def destroy(Title:str,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.title==Title)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the title {Title} is not available')
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the title {Title} is removed')