from pydantic import BaseModel
from typing import List

class QuestionRequest(BaseModel):
    titleSlug: str

class QuestionResponse(BaseModel):
    questionId: str
    questionFrontendId: str
    title: str
    titleSlug: str
    isPaidOnly: bool
    difficulty: str
    likes: int
    dislikes: int
    content: str

class SimilarQuestion(BaseModel):
    difficulty: str
    titleSlug: str
    title: str
    translatedTitle: str | None
    isPaidOnly: bool

class SimilarQuestionsResponse(BaseModel):
    similarQuestionList: List[SimilarQuestion]