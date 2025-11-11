from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from ..models import ExpenseCreate
from .. import crud

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", status_code=201)
async def create_expense(payload: ExpenseCreate):
    doc = payload.dict()
    new_id = await crud.create_expense(doc)
    return {"id": new_id}

@router.get("/")
async def list_expenses(
        category: Optional[str] = Query(None, description="Filter by category"),
        from_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
        to_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)"),
        limit: int = Query(100, ge=1, le=1000, description="Maximum number of expenses to return")
    ):

    query = {}
    if category:
        query["category"] = {"$regex": f"^{category}$", "$options": "i"}

    date_filter = {}
    if from_date:
        try:
            from_dt = datetime.strptime(from_date, "%Y-%m-%d")
            date_filter["$gte"] = from_dt
        except ValueError:
            raise ValueError("Invalid from_date format. Use YYYY-MM-DD.")
    if to_date:
        try:
            to_dt = datetime.strptime(to_date, "%Y-%m-%d")
            date_filter["$lte"] = to_dt
        except ValueError:
            raise ValueError("Invalid to_date format. Use YYYY-MM-DD.")

    if date_filter:
        query["date"] = date_filter

    expenses = await crud.list_expenses(query=query, limit=limit)
    return expenses

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
