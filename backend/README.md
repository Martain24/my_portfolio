# Backend - FastAPI

---

## Structure

app/main.py → FastAPI entrypoint.  
app/core/ → config and utilities.  
app/routers/ → route groups.  
app/models/ → database models.  

---

## Routers

### Basic Projects

Path prefix: `/basic-projects`. 

#### Calculator
- `GET /basic-projects/calculator/{expression}` → evaluate a mathematical expression.

