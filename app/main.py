from fastapi import FastAPI

app = FastAPI(title="NotificationHub")

@app.get("/")
async def home():
    return {"message": "NotificationHub API is running"}