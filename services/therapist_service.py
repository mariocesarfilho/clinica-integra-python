from sqlalchemy.orm import Session
from sqlalchemy import Integer
from models.therapist import Therapist
from schemas.therapist import TherapistCreate, TherapistPatch

def create_therapist(db: Session, data: TherapistCreate):
  db_therapist = Therapist(**data.model_dump())

  db.add(db_therapist)
  db.commit()
  db.refresh(db_therapist)

  return db_therapist

def get_therapist(db: Session, therapist_id: int):
  return db.query(Therapist).filter(Therapist.id == therapist_id).first()

def put_therapist(db: Session, therapist_id: int, data: TherapistCreate):
  db_therapist = db.query(Therapist).filter(Therapist.id == therapist_id).first()

  if not db_therapist:
    return None
  
  new_therapist = data.model_dump(exclude_unset=True)

  for key, value in new_therapist.items():
    setattr(db_therapist, key, value)

  db.commit()
  db.refresh(db_therapist)

  return db_therapist

def patch_therapist(db: Session, therapist_id: int, data: TherapistPatch):
  db_therapist = db.query(Therapist).filter(Therapist.id == therapist_id).first()

  if not db_therapist:
    return None
  
  new_therapist = data.model_dump(exclude_unset=True)

  for key, value in new_therapist.items():
    setattr(db_therapist, key, value)

  db.commit()
  db.refresh(db_therapist)

  return db_therapist
