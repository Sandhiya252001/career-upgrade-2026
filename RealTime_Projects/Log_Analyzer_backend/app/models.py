from app.database import Base
from sqlalchemy import Column,String,Integer
class Log(Base):
    __tablename__="logs"
    id=Column(Integer,index=True,primary_key=True)
    timestamp=Column(String,nullable=False)
    log_level=Column(String,nullable=False)
    message=Column(String,nullable=False)
