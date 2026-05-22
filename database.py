from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "postgresql://postgres:123456@localhost:5432/clinica_db"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()