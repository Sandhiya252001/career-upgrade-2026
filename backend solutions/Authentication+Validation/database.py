from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
DB_URL="sqlite:///./logs.db"
engine=create_engine(DB_URL,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine,autoflush=False, autocommit=False)
base=declarative_base()
