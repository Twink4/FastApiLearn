from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'title' : 'index',
            'program_versiobn': '0.0.1'}

@app.get('/about_us')
def about_us():
    return {
        'title': 'About us',
        'text': 'I am Alex.',
        'mail': 'A@aa.a'
    }