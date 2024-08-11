from pydantic import BaseModel

class QuestionStatsRequest(BaseModel):
    titleSlug: str

class QuestionStats(BaseModel):
    stats: str

class QuestionStatsResponse(BaseModel):
    question: QuestionStats