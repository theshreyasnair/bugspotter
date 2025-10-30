# imports
from fastapi import FastAPI
from models import TracebackInput

app = FastAPI()

@app.get('/')
def home():
    return {"message" : "Hello, world"}

@app.get('/health')
def health():
    return {"message" : "health route"}

@app.get('/analyze')
def analyze(traceback: TracebackInput):
    return {"traceback" : f"Received {traceback.traceback}"}