from fastapi import FastAPI
from app.routers import expenses

app = FastAPI(title="Expense Tracker App")

app.include_router(expenses.router)


# simple root
@app.get("/")
async def root():
    return {"message": "Expense Tracker - no login required"}


# # run with uvicorn in Docker
# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
