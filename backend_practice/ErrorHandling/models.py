from database import base
from sqlalchemy import Column,String,Integer
class Logging(base):
    __tablename__="MyLog"
    id=Column(Integer,index=True,primary_key=True)
    type=Column(String)
    message=Column(String)

    