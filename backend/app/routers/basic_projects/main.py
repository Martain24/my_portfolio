from fastapi import APIRouter
from .calculator.router import router as calculator_router

router = APIRouter(
    prefix="/basic-projects",
    tags=["Basic Projects"]
)

router.include_router(calculator_router, prefix="/calculator")
