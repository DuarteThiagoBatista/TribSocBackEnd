from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://gvsqznpkutpked:6874da7fc19ffdcab2b54a7afc15993fd4396b2278ebc5e28dffb6d6b4cf1c1c@ec2-54-165-184-219.compute-1.amazonaws.com:5432/dantq1ttsd6l9a"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_db():
  Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()