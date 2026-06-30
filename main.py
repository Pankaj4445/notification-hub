from fastapi import FastAPI

app = FastAPI(title="NotificationHub")

@app.get("/")
async def home():
    return {"message": "NotificationHub API is running"}

from app.redis.client import redis_client

redis_client.set("test", "hello")
print(redis_client.get("test"))