from sqlalchemy import Column, Integer, String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__='blogs'
    
    #id=Column(Integer, primary_key=True, index=True)
    title= Column(String, primary_key=True, index=True)
    body=Column(String)
    user_id=Column(Integer,ForeignKey('User.email'))


    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__='User'

    #id=Column(Integer, primary_key=True, index=True)
    name=Column(String, primary_key=True, index=True)
    email=Column(String)
    password=Column(String)

    blogs = relationship("Blog", back_populates="creator")
 