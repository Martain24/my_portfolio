from fastapi import APIRouter, HTTPException
from fastapi import status

router = APIRouter()

@router.get("/{expression}")
def evaluate_expression(expression: str):
    try:
        result = eval(expression)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": f"Invalid mathematical expression: {expression}"}
        )
    
    if not isinstance(result, (int, float)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": f"Expression does not evaluate to a number: {expression}"}
        )
    
    return {
        "expression": expression,
        "result": result
    }
        