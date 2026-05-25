from pydantic import BaseModel, ConfigDict
from typing import Optional

class TherapistBase(BaseModel):
  name: str
  cpf: str
  email: str
  password: str

class TherapistCreate(TherapistBase):
  pass

class TherapistPatch(TherapistBase):
  name: Optional[str] = None
  cpf: Optional[str] = None
  email: Optional[str] = None
  password: Optional[str] = None

class TherapistGet(TherapistBase):
  id: int
  model_config = ConfigDict(from_attributes=True)