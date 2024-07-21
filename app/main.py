from fastapi import FastAPI
from app.api.endpoints import question

app = FastAPI(title="LeetCode API Wrapper")

app.include_router(question.router, prefix="/api", tags=["questions"])