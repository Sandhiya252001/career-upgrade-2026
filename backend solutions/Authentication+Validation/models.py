from database import base
from sqlalchemy import Column,String,Integer
class Log(base):
    __tablename__="Logs"
    id=Column(Integer,primary_key=True,index=True)
    level=Column(String,index=True)
    message=Column(String)