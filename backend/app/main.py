from fastapi import FastAPI
from app.routers.basic_projects.main import router as basic_projects_router

app = FastAPI()

app.include_router(basic_projects_router)
