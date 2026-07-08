from fastapi import FastAPI
from app.api.v1.auth import router as auth_router

app = FastAPI(title="NotificationHub")
app.include_router(auth_router)

@app.get("/")
async def home():
    return {"message": "NotificationHub API is running"}

from app.redis.client import redis_client

redis_client.set("test", "hello")
print(redis_client.get("test"))