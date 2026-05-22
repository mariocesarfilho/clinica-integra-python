from fastapi import FastAPI
from routers import therapist_router

app = FastAPI(
  title="API Clinica Integra Phyton",
  description="Sistema de gestão para clínica terapêuta",
  version="1.0.0"
)

app.include_router(therapist_router.router, prefix="/therapist", tags=["Therapists"])

@app.get("/")
def health_check():
  return { "status": "online" }