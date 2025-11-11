from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ExpenseCreate(BaseModel):
    title: str = Field(..., max_length=100, description="Title of the expense")
    amount: float = Field(..., gt=0, description="Amount of the expense")
    category: Optional[str] = Field(
        None, max_length=50, description="Category of the expense"
    )
    date: datetime = Field(
        default_factory=datetime.utcnow, description="Date of the expense"
    )
    notes: Optional[str] = Field(
        None, max_length=500, description="Additional notes about the expense"
    )


class Expense(ExpenseCreate):
    id: str = Field(..., alias="_id")
