from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
db_url="sqlite:///./logs.db"
engine=create_engine(db_url,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
