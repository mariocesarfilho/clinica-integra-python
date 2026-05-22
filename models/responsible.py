from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .person import Person
from .associations import patient_responsible

class Responsible(Person):
  __tablename__ = "responsibles"

  email = Column(String, unique=True, nullable=True)
  relationship_patient = Column(String)
  patients = relationship("Patient", secondary=patient_responsible, back_populates="responsibles")