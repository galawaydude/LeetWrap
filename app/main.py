from fastapi import FastAPI
from app.api.endpoints import question, stats

app = FastAPI(
    title="LeetCode API Wrapper",
    description="A FastAPI wrapper for LeetCode's GraphQL API",
    version="1.0.0"
)

app.include_router(question.router, prefix="/api", tags=["questions"])
app.include_router(stats.router, prefix="/api", tags=["stats"])