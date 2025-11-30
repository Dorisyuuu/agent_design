from pydantic import BaseModel

class GenerateRequest(BaseModel):
    input: str

class GenerateResponse(BaseModel):
    draft: str
    refined: str
