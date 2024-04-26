from fastapi import FastAPI

app= FastAPI()


@app.get('/')
def index():
    return {'data':{'abhay':1,'haldiya': 2}}


@app.get('/about')
def about():
    return {'data':"hi i am about"}
