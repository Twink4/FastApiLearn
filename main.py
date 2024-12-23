from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'title' : 'index',
            'program_versiobn': '0.0.1'}