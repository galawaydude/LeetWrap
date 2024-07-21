from pydantic import BaseModel

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