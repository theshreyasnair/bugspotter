# imports
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .models import TracebackInput
from .parsers.traceback_parser import parse_traceback

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))

@app.get('/')
def home():
    return {"message" : "Hello, world"}

@app.get('/health')
def health():
    return {"message" : "health route"}

@app.post('/analyze')
def analyze(traceback: TracebackInput):
    return parse_traceback(traceback.traceback)

@app.get('/submit')
def submit(request: Request):
    return templates.TemplateResponse("submit.html", {"request": request})
