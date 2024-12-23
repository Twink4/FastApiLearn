from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'title' : 'index',
            'program_version': '0.0.1'}