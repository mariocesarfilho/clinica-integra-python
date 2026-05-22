from pydantic import BaseModel
from typing import Optional

class TherapistCreate(BaseModel):
  name: str
  cpf: str
  email: str
  password: str

class TherapistPatch(BaseModel):
  name: Optional[str] = None
  cpf: Optional[str] = None
  email: Optional[str] = None
  password: Optional[str] = None
