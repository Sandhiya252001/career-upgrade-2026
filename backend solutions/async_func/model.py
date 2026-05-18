from database import Base
from sqlalchemy import Column,Integer,String
class logClass(Base):
    __tablename__="logTable"
    id=Column(Integer,primary_key=True,index=True)
    level=Column(String)
    message=Column(String)

