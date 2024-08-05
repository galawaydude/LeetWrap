from pydantic import BaseModel, Field
from typing import List, Optional


class recentAc(BaseModel):
    id: str
    title: str
    titleSlug: str
    timestamp: str

class recentAcResponse(BaseModel):
     recentAcSubmissionList: List[recentAc]

class recentAcRequest(BaseModel):
    username: str
    limit: int
    leetcodeSession: str = Field(..., description="This is the leetcode cookie, that i will be using for the authentication, ")