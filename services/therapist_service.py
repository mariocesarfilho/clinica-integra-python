from sqlalchemy.orm import Session
from sqlalchemy import Integer
from models.therapist import Therapist
from schemas.therapist import TherapistCreate

def create_therapist(db: Session, data: TherapistCreate):
  db_therapist = Therapist(**data.model_dump())

  db.add(db_therapist)
  db.commit()
  db.refresh(db_therapist)

  return db_therapist

def get_therapist(db: Session, therapist_id: int):
  return db.query(Therapist).filter(Therapist.id == therapist_id).first()