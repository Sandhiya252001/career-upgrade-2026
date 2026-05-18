from pydantic import BaseModel,Field
from typing import Literal
class Logger(BaseModel):
    level:Literal["ERROR","WARNING","INFO"]
    message:str=Field(...,min_length=1)
    