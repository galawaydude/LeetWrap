from pydantic import BaseModel, Field
from typing import Optional

class QuestionNote(BaseModel):
    questionId: str
    note: Optional[str]

class QuestionNoteResponse(BaseModel):
    question: QuestionNote

class QuestionNoteRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")