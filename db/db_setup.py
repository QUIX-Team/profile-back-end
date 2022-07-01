from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:222000@localhost/pharos"


engine = create_engine('postgresql://postgres:222000@localhost/pharos')
Session = sessionmaker(bind=engine)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

# DB_Utilties 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()