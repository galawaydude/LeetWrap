from pydantic import BaseModel, Field
from typing import Optional

class QuestionStatus(BaseModel):
    status: Optional[str]

class UserQuestionStatusResponse(BaseModel):
    question: QuestionStatus

class UserQuestionStatusRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")