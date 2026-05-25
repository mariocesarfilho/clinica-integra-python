from sqlalchemy import Column, String, Boolean, Date
from sqlalchemy.orm import relationship
from .person import Person
from .associations import patient_responsible

class Patient(Person):
  __tablename__ = "patients"

  # Tabela
  # Nome
  # CPF
  # Data de Nascimento
  # Plano de Saúde
  # Diagnóstico
  # Medicação
  # Pais Casados
  # Responsável

  cpf = Column(String, unique=True, nullable=False)
  birthday = Column(Date, nullable=False)
  health_insurance = Column(Boolean, nullable=False)
  diagnosis = Column(String, nullable=True)
  medication = Column(String, nullable=True)
  married_parents = Column(Boolean, nullable=False)
  responsibles = relationship("Responsible", secondary=patient_responsible, back_populates="patients")
