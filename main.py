from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'sdfsdf'

@app.get('/sd')
def index():
    return 'sdfsdf'