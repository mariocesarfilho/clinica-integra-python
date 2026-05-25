from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date
from schemas.responsible import ResponsibleGet

class PatientBase(BaseModel):
  name: str
  cpf: str
  birthday: date
  health_insurance: bool
  diagnosis: Optional[str] = None
  medication: Optional[str] = None
  married_parents: bool

class PatientCreate(PatientBase):
  responsible_ids: List[int] = []

class PatientPatch(PatientBase):
  name: Optional[str] = None
  cpf: Optional[str] = None
  birthday: Optional[date] = None
  health_insurance: Optional[bool] = None
  diagnosis: Optional[str] = None
  medication: Optional[str] = None
  married_parents: Optional[bool] = None
  responsible_ids: Optional[List[int]] = None

class PatientGet(PatientBase):
  id: int
  responsibles: List[ResponsibleGet] = []
  model_config = ConfigDict(from_attributes=True)