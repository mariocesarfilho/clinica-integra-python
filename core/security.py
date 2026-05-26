import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

SECRET_KEY = "key_secret"
ALGORITHIM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

def get_password(password: str):
  return pwd_context.hash(password)

def verify_password(hashed_password: str, plain_password: str):
  return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHIM)
  return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
  credentails_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expirado!",
    headers={"WWW-Authenticate": "Bearer"},
  )

  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHIM)

    user_id: str = payload.get("sub")

    if user_id is None:
      raise credentails_exception

    return user_id
  
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado, faça login novamente!")
  except jwt.InvalidTokenError:
    raise create_access_token