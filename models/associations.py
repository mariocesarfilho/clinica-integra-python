from sqlalchemy import Table, Column, Integer, ForeignKey
from .person import Base

patient_responsible = Table(
  "paciente_responsible",
  Base.metadata,
  Column("patient_id", Integer, ForeignKey("patients.id"), primary_key=True),
    Column(
        "responsible_id", Integer, ForeignKey("responsibles.id"), primary_key=True
    ),
)