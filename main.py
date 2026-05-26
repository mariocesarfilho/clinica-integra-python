from fastapi import FastAPI
from routers.api_v1 import router as api_v1_router

app = FastAPI(
  title="API Clinica Integra Phyton",
  description="Sistema de gestão para clínica terapêuta",
  version="1.0.0"
)
app.include_router(api_v1_router)

@app.get("/")
def health_check():
  return { "status": "online" }