from fastapi import FastAPI
from .api import router as api_router

app = FastAPI(
    title="My GitHub App",
    version="1.0.0",
    description="A minimal FastAPI application."
)

@app.get("/")
def root():
    return {"message": "App is running"}

app.include_router(api_router, prefix="/api")
