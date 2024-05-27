from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from ..import schemas,models,oauth2
from ..database import SessionLocal,get_db
from ..hashing import Hash
from ..repository import user

router=APIRouter(
    prefix="/user",
    tags=['User']
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request :schemas.User, db:Session=Depends(get_db)):
    return user.create_user(request,db)

@router.get('/{umail}',response_model=schemas.ShowUser)
def get_user(umail:str,upassword:str, db: Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get_user(umail,upassword,db)

#######################  delete_user, update_user
@router.put('/{umail}',response_model=schemas.ShowUser1, status_code=status.HTTP_202_ACCEPTED)
def update_user(umail:str,upassword:str,request :schemas.User,db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.update(umail,upassword,request,db)


@router.delete('/{umail}')
def delete_user(umail:str,upassword:str,db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.destroy(umail,upassword,db)