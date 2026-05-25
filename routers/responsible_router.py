from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db
from schemas.responsible import ResponsibleCreate, ResponsiblePatch, ResponsibleGet
from services import responsible_service

router = APIRouter()

@router.get("/{id}", response_model=ResponsibleGet, status_code=200)
def show(id: int, db: Session = Depends(get_db())):
  db_responsible = responsible_service.get_responbile(db=db, responsible_id=id)

  if db_responsible is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Responsável não encontrado!")
  
  return db_responsible

@router.post("/", response_model= ResponsibleGet, status_code=status.HTTP_201_CREATED)
def create(responsible: ResponsibleCreate, db: Session = Depends(get_db())):
  db_responsible = responsible_service.create_responsible(db=db, data=responsible)
  
  return db_responsible

@router.patch("/{responsible_id}", response_model=ResponsibleGet, status_code=status.HTTP_200_OK)
def update(id: int, responsible: ResponsiblePatch, db: Session = Depends(get_db())):
  db_responsible = responsible_service.patch_responsible(db=db, responsible_id=id, data=responsible)

  if db_responsible is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Erro ao tentar atualizar Responsável")
  
  return db_responsible

@router.delete("/{responsible_id}", status_code=status.HTTP_200_OK)
def delete(id: int, db: Session = Depends(get_db())):
  db_responsible = responsible_service.delete_responsible(db=db, responsible_id=id)

  if not db_responsible:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Erro ao tentar excluir Responsável!")
  
  return Response(status_code=status.HTTP_204_NO_CONTENT)