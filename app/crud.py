from unicodedata import category
from .db import expenses_collection
from bson import ObjectId
from datetime import datetime,timezone
from fastapi import HTTPException, status

async def create_expense(doc):

    if doc.get("date") is None:
        doc["date"] = datetime.now(timezone.utc)

    existing = await expenses_collection.find_one({"title": doc["title"]})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Expense with title '{doc['title']}' already exists today."
        )
    res = await expenses_collection.insert_one(doc)
    doc["_id"] = str(res.inserted_id)
    return doc

async def get_expense(expense_id):
    doc = await expenses_collection.find_one({"_id": ObjectId(expense_id)})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

async def list_expenses(query: dict = None,limit=10):
    if query is None:
        query = {}
        
    cursor = expenses_collection.find(query).sort("date", -1).limit(limit)
    docs = []
    async for d in cursor:
        d["_id"] = str(d["_id"])
        docs.append(d)
    return docs

async def delete_expense(expense_id):
    res = await expenses_collection.delete_one({"_id": ObjectId(expense_id)})
    return res.deleted_count


async def get_summary(query: dict = None):
    if query is None:
        query = {}

    pipeline = [
        {"$match": query},
        {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}},
        {"$sort": {"total": -1}}
    ]

    cursor = expenses_collection.aggregate(pipeline)
    summary = []
    async for doc in cursor:
        summary.append({
            "category": doc["_id"],
            "total": doc["total"]
        })
    return summary