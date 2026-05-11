from pydantic import BaseModel,Field
from typing import Literal
class LogCreate(BaseModel):
    level:Literal["INFO","WARNIG","ERROR"]
    message:str=Field(...,min_length=1)
