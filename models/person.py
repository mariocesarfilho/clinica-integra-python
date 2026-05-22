from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Person(Base):
  __abstract__ = True

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True, nullable=False)
