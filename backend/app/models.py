from pydantic import BaseModel

class TracebackInput(BaseModel):
    traceback: str