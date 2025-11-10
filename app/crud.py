from .db import expenses_collection
from bson import ObjectId
from datetime import datetime,timezone

async def create_expense(doc):
    if not doc.get("date"):
        doc["date"] = datetime.now(timezone.utc)
    res = await expenses_collection.insert_one(doc)
    return str(res.inserted_id)

async def get_expense(expense_id):
    doc = await expenses_collection.find_one({"_id": ObjectId(expense_id)})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

async def list_expenses(limit=10):
    cursor = expenses_collection.find().sort("date", -1).limit(limit)
    docs = []
    async for d in cursor:
        d["_id"] = str(d["_id"])
        docs.append(d)
    return docs

async def delete_expense(expense_id):
    res = await expenses_collection.delete_one({"_id": ObjectId(expense_id)})
    return res.deleted_count