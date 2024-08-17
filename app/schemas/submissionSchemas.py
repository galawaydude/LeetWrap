from pydantic import BaseModel, Field
from typing import List, Optional

class TopicTag(BaseModel):
    id: str
    name: str
    slug: str
    translatedName: Optional[str] = None

class Submission(BaseModel):
    runtime: str
    memory: str
    timestamp: int
    status: int
    statusDisplay: str
    lang: str
    langName: str
    notes: Optional[str] = None
    id: str
    hasNotes: bool
    topicTags: List[TopicTag]

class SubmissionListResponse(BaseModel):
    lastKey: Optional[str] = None
    hasNext: bool
    submissions: List[Submission]

class SubmissionListRequest(BaseModel):
    questionSlug: str
    limit: int
    offset: int
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

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