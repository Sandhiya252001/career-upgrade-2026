from database import sessionmaker,base
from sqlalchemy import Column,Integer,String
class Logs(base):
    __tablename__="logTable"
    id=Column(Integer,primary_key=True,index=True)
    level=Column(String)
    message=Column(String)
    
    
