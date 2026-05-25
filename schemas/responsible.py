from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class ResponsibleBase(BaseModel):
  name: str
  email: str
  relationship_patient: str

class ResponsibleCreate(ResponsibleBase):
  pass

class ResponsiblePatch(ResponsibleBase):
  name: Optional[str] = None
  email: Optional[str] = None
  relationship_patient: Optional[str] = None

class ResponsibleGet(ResponsibleBase):
  id: id

  model_config = ConfigDict(from_attributes=True)