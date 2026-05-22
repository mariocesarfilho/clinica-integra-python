from pydantic import BaseModel

class TherapistCreate(BaseModel):
  name: str
  cpf: str
  email: str
  password: str
