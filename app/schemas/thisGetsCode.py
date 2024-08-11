from pydantic import BaseModel, Field
from typing import List, Optional

class UserProfile(BaseModel):
    realName: Optional[str]
    userAvatar: Optional[str]

class User(BaseModel):
    username: str
    profile: UserProfile

class Lang(BaseModel):
    name: str
    verboseName: str

class Question(BaseModel):
    questionId: str

class TopicTag(BaseModel):
    tagId: str
    slug: str
    name: str

class SubmissionDetails(BaseModel):
    runtime: int
    runtimeDisplay: str
    runtimePercentile: float
    runtimeDistribution: str
    memory: int
    memoryDisplay: str
    memoryPercentile: float
    memoryDistribution: str
    code: str
    timestamp: int
    statusCode: int
    user: User
    lang: Lang
    question: Question
    notes: Optional[str]
    topicTags: List[TopicTag]
    runtimeError: Optional[str]
    compileError: Optional[str]
    lastTestcase: Optional[str]

class SubmissionDetailsResponse(BaseModel):
    submissionDetails: SubmissionDetails

class SubmissionDetailsRequest(BaseModel):
    submissionId: int
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")