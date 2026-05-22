from sqlalchemy import Column, String
from .person import Person

class Therapist(Person):
  __tablename__ = "therapists"

  email = Column(String, index=True, unique=True, nullable=False)
  cpf = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)