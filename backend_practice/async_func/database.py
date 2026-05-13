from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
db_url="sqlite:///./logger.db"
engine=create_engine(db_url,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()