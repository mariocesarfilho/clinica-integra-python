from sqlalchemy import Integer
from sqlalchemy.orm import Session
from models.responsible import Responsible
from schemas.responsible import ResponsibleCreate, ResponsiblePatch, ResponsibleGet

def create_responsible(db: Session, data: ResponsibleCreate):
  db_responsible = Responsible(**data.model_dump())

  db.add(db_responsible)
  db.commit()
  db.refresh(db_responsible)

  return db_responsible

def get_responbile(db: Session, responsible_id: int):
  return db.query(Responsible).filter(Responsible.id == responsible_id.id)

def patch_responsible(db: Session, data: ResponsiblePatch, responsible_id: int):
  selected_responsible = db.query(Responsible).filter(Responsible.id == responsible_id.id).first()

  if not selected_responsible:
    return None
  
  new_responsible = data.model_dump(exclude_unset=True)

  for key, value in new_responsible.items():
    setattr(selected_responsible, key, value)

  db.commit()
  db.refresh(selected_responsible)

  return selected_responsible

def delete_responsible(db: Session, responsible_id: int):
  selected_responsible = db.query(Responsible).filter(Responsible.id == responsible_id.id).first()

  if not selected_responsible:
    return None

  db.delete(selected_responsible)
  db.commit()

  return True

