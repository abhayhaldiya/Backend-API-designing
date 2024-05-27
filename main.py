from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel

app= FastAPI()


@app.get('/')
def index():
    return {'data':{'abhay':1,'haldiya': 2}}

@app.get('/blog')
def index(limit: int= 10,published: bool=True):
    if(published==True):
        return {'data':f'{limit} published blogs'}
    else:
        return {'data':f'{limit} blog'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def blog(id: int):
    return {'data':id  }

class Base(BaseModel):
    title:str
    body:str
    published: Optional[bool]

@app.post('/blog')
def create_blog(body: Base):
    return {f'blog is created wiht tilte as {body.title}'}



















# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1", port=9000)