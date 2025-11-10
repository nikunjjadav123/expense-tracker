from motor.motor_asyncio import AsyncIOMotorClient
import os
import dotenv

dotenv.load_dotenv() 

MONGO_URL = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(MONGO_URL)

db = client.get_default_database()
expenses_collection = db.expenses
