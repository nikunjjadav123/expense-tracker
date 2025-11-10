from fastapi import APIRouter, HTTPException
from ..models import ExpenseCreate
from .. import crud

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", status_code=201)
async def create_expense(payload: ExpenseCreate):
    doc = payload.dict()
    new_id = await crud.create_expense(doc)
    return {"id": new_id}

@router.get("/")
async def list_expenses(limit: int = 100):
    return await crud.list_expenses(limit=limit)

@router.get("/{expense_id}")
async def get_expense(expense_id: str):
    doc = await crud.get_expense(expense_id)
    if not doc:
        raise HTTPException(404, "Not found")
    return doc

@router.delete("/{expense_id}", status_code=204)
async def delete_expense(expense_id: str):
    deleted = await crud.delete_expense(expense_id)
    if deleted == 0:
        raise HTTPException(404, "Not found")
    return {}
