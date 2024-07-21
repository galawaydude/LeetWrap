from pydantic import BaseModel, Field
from typing import List, Optional, Union

class TopicTag(BaseModel):
    id: str
    name: str
    slug: str
    translatedName: Optional[str] = None

class Submission(BaseModel):
    runtime: str
    memory: str
    timestamp: int
    status: Union[str, int]
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