# from typing import List
# from fastapi import APIRouter,Depends,status,HTTPException,Response
# from . import schemas, database, models, oauth2
# from sqlalchemy.orm import Session
# from .repository import blog
# from .database import get_db


#     # user=db.query(models.User).filter(models.User.id==id).first()
#     #userid=user.id


# @router.post('/', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.Useridd = Depends(oauth2.get_current_user)):
#     userid=current_user.id
#     return blog.create(request, db,userid)

# def create(request: schemas.Blog,db:Session,userid):
#     new_blog=models.Blog(title=request.title, body=request.body,user_id=userid)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog



# # @router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
# # def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
# #     return blog.show(id,db)

# # def show(id:int,response:Response, db:Session):
# #     blog=db.query(models.Blog).filter(models.Blog.id==id).first()
# #     if not blog:
# #          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
# #     #    response.status_code=status.HTTP_404_NOT_FOUND
# #     #    return{"detail":f'blog with the id {id} is not available'}
# #     return blog
