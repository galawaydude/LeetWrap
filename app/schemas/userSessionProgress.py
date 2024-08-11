from pydantic import BaseModel, Field
from typing import List

class CountByDifficulty(BaseModel):
    difficulty: str
    count: int

class SubmissionCount(BaseModel):
    difficulty: str
    count: int
    submissions: int

class SubmitStats(BaseModel):
    acSubmissionNum: List[SubmissionCount]
    totalSubmissionNum: List[SubmissionCount]

class MatchedUser(BaseModel):
    submitStats: SubmitStats

class UserSessionProgressResponse(BaseModel):
    allQuestionsCount: List[CountByDifficulty]
    matchedUser: MatchedUser

class UserSessionProgressRequest(BaseModel):
    username: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")