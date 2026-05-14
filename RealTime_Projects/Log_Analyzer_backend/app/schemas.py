from pydantic import BaseModel
class LogResponse(BaseModel):
    id:int
    timestamp:str
    log_level:str
    message:str
    class Config:
        form_attributes=True
class StatsResponse(BaseModel):
    total_logs: int
    info_count: int
    warning_count: int
    error_count: int

