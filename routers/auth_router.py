from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from sqlalchemy.orm import Session

from models.therapist import Therapist
from core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags="Authorization")

@router.post("/", status_code=status.HTTP_200_OK)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db())):
  therapist = db.query(Therapist).filter(Therapist.email == form_data.username).first()

  if not therapist or not verify_password(form_data.password, therapist.password):
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail="Erro! Usuário não encontrado.", 
      headers={"WWW-Authenticate": "Bearer"},
      )
  
  access_token = create_access_token(data={"sub": str(therapist.id)})

  return { "access_token": access_token, "token_type": "bearer" }