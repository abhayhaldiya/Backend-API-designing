from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from ..import models,schemas
from ..hashing import Hash


def create_user(request :schemas.User, db:Session):
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(umail:str,upassword:str, db: Session):
    user=db.query(models.User).filter(models.User.email==umail).first()
    user1=user.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the email {umail} is not available')
    if not Hash.verify(upassword,user1.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect Password')
    return user


def update(umail:str,upassword:str,request :schemas.User,db:Session):
    user=db.query(models.User).filter(models.User.email==umail)
    user1=user.first()
    
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the email {umail} is not available')
    if not Hash.verify(upassword,user1.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect Password')
    user.update({'name':request.name,'email':request.email,'password':Hash.bcrypt(request.password)})
    db.commit()
    return user

def destroy(umail:str,upassword:str,db:Session):
    user=db.query(models.User).filter(models.User.email==umail)
    user1=user.first()
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the email {umail} is not available')
    if not Hash.verify(upassword,user1.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect Password')
    else:
        user.delete(synchronize_session=False)
        db.commit()
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED,detail=f'user with the email {umail} is deleted')