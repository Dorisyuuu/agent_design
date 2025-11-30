from typing import Optional
from pydantic import BaseModel

class GraphState(BaseModel):
    user_input: str
    draft: Optional[str] = None
    refined: Optional[str] = None
