from pydantic import BaseModel
from typing import List

class QuestionHintsRequest(BaseModel):
    titleSlug: str

class QuestionHints(BaseModel):
    hints: List[str]

class QuestionHintsResponse(BaseModel):
    question: QuestionHints