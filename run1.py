import uvicorn
from fastapi import FastAPI, Depends
from flyingbirds import application

app = FastAPI(
    title='FastAPI  tutoral  API docs',
    description='bridproject',
    version= '1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',


)


app.include_router(application,prefix='/flyingbirds',tags=['鸟'])
if __name__ == '__main__':
    uvicorn.run('run1:app', host='localhost', port=8000, reload=True, workers=1)
