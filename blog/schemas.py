from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class Config():
        orm_mode=True



class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]=[]
    class Config():
        orm_mode=True


class ShowUser1(BaseModel):
    blogs:List[Blog]=[]
    class Config():
        orm_mode=True


class ShowBlog(BaseModel):
    title:str
    body:str
    creator: ShowUser
    class Config():
        orm_mode=True


class Login(BaseModel):
    username:str
    password:str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None













# class Blog(BaseModel):
#     title:str
#     body:str


# class ShowBlog(BaseModel):
#     title:str
#     class Config():
#         orm_mode=True

# #this would allow to pass only thoses atributes which are passed in the response model/schema
# # or we can right the above function as:

# # class ShowBlog(Blog):
# #     class Config():
# #         orm_mode=True

