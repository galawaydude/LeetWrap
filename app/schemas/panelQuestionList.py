from pydantic import BaseModel, Field
from typing import List, Optional

class TopicTag(BaseModel):
    name: str
    slug: str

class Question(BaseModel):
    difficulty: str
    id: int
    paidOnly: bool
    questionFrontendId: str
    status: Optional[str]
    title: str
    titleSlug: str
    topicTags: List[TopicTag]
    score: Optional[float] = None
    questionNumber: Optional[int] = None

class PanelQuestionList(BaseModel):
    hasViewPermission: bool
    panelName: str
    finishedLength: int
    totalLength: int
    questions: List[Question]

class PanelQuestionListResponse(BaseModel):
    panelQuestionList: PanelQuestionList

class PanelQuestionListRequest(BaseModel):
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")