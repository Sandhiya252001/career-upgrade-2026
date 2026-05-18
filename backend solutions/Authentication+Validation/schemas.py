from pydantic import BaseModel,Field
from typing import Literal
class LogCreate(BaseModel):
    level:Literal["INFO","ERROR","WARNING"]
    message:str=Field(...,min_length=1)