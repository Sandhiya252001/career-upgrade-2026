from sqlalchemy import Column,Integer,String
from database import Base
class Log(Base):
    __tablename__="Logs"
    id=Column(Integer,primary_key=True,index=True)
    level=Column(String)
    message=Column(String)
    