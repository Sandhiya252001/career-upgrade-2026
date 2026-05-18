from database import Base
from sqlalchemy import Column,Integer,String,Float
class Employee(Base):
    __tablename__="emp"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    department=Column(String)
    salary=Column(Float)

