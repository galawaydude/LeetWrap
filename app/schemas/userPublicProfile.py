from pydantic import BaseModel
from typing import List, Optional

class Profile(BaseModel):
    ranking: int
    userAvatar: str
    realName: str
    aboutMe: str
    school: Optional[str]
    websites: List[str]
    countryName: Optional[str]
    company: Optional[str]
    jobTitle: Optional[str]
    skillTags: List[str]
    postViewCount: int
    postViewCountDiff: int
    reputation: int
    reputationDiff: int
    solutionCount: int
    solutionCountDiff: int
    categoryDiscussCount: int
    categoryDiscussCountDiff: int

class MatchedUser(BaseModel):
    contestBadge: Optional[dict]
    username: str
    githubUrl: Optional[str]
    twitterUrl: Optional[str]
    linkedinUrl: Optional[str]
    profile: Profile

class UserPublicProfileResponse(BaseModel):
    matchedUser: MatchedUser

class UserPublicProfileRequest(BaseModel):
    username: str