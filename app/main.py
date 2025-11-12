from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import expenses

app = FastAPI(title="Expense Tracker App")

# ✅ define CORS first
origins = [
    "https://expense-tracker-frontside.onrender.com",
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

# ✅ include routers after CORS
app.include_router(expenses.router)


@app.get("/")
async def root():
    return {"message": "Expense Tracker - no login required"}
