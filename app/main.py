from fastapi import FastAPI
from app.routers import expenses
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Expense Tracker App")

app.include_router(expenses.router)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# simple root
@app.get("/")
async def root():
    return {"message": "Expense Tracker - no login required"}


# # run with uvicorn in Docker
# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
