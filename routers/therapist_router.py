from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db
from schemas.therapist import TherapistCreate, TherapistPatch, TherapistGet
from services import therapist_service

router = APIRouter()

@router.post("/", response_model=TherapistGet, status_code=status.HTTP_201_CREATED)
def create(therapist: TherapistCreate, db: Session = Depends(get_db)):
  new_therapist = therapist_service.create_therapist(db=db, data=therapist)
  return new_therapist

@router.get("/{therapist_id}", response_model=TherapistGet, status_code=status.HTTP_200_OK)
def show(therapist_id: int, db: Session = Depends(get_db)):
  db_therapist = therapist_service.get_therapist(db=db, therapist_id=therapist_id)

  if db_therapist is None: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Terapeuta não encontrado!")
  
  return db_therapist

@router.patch("/{therapist_id}", response_model=TherapistGet, status_code=status.HTTP_200_OK)
def update_patch(therapist_id: int, therapist: TherapistPatch, db: Session = Depends(get_db)):
  db_therapist = therapist_service.patch_therapist(db=db, therapist_id=therapist_id, data=therapist)

  if db_therapist is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Erro ao atualizar terapeuta!")
  
  return db_therapist

@router.delete("/{therapist_id}", status_code=status.HTTP_200_OK)
def delete_therapist(therapist_id: int, db: Session = Depends(get_db)):
  db_therapist = therapist_service.delete_therapist(db=db, therapist_id=therapist_id)

  if not db_therapist:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Erro ao tentar deletar Terapeuta!")

  return Response(status_code=status.HTTP_204_NO_CONTENT)