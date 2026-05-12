from pydantic import BaseModel,Field
from typing import Literal
class Logger(BaseModel):
    type:Literal["INFO","WARNING","ERROR"]
    message:str=Field(...,min_length=1)
