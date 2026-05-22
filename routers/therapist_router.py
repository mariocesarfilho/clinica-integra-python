from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.therapist import TherapistCreate
from services import therapist_service

router = APIRouter()

@router.post("/", status_code=201)
def create(therapist: TherapistCreate, db: Session = Depends(get_db)):
  new_therapist = therapist_service.create_therapist(db=db, data=therapist)
  return new_therapist

@router.get("/{therapist_id}", status_code=200)
def show(therapist_id: int, db: Session = Depends(get_db)):
  db_therapist = therapist_service.get_therapist(db, therapist_id)

  if db_therapist is None: 
    raise HTTPException(status_code=404, detail="Terapeuta não encontrado!")
  
  return db_therapist