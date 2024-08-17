from pydantic import BaseModel, Field
from typing import List, Optional

# UserPublicProfile schemas
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

# UserSessionProgress schemas
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

class MatchedUserProgress(BaseModel):
    submitStats: SubmitStats

class UserSessionProgressResponse(BaseModel):
    allQuestionsCount: List[CountByDifficulty]
    matchedUser: MatchedUserProgress

class UserSessionProgressRequest(BaseModel):
    username: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

# UserFavorites schemas
class Question(BaseModel):
    titleSlug: str

class Favorite(BaseModel):
    idHash: str
    name: str
    isPublicFavorite: bool
    questions: List[Question]

class FavoritesList(BaseModel):
    allFavorites: List[Favorite]

class UserFavoritesResponse(BaseModel):
    favoritesLists: FavoritesList

class UserFavoritesRequest(BaseModel):
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

# StreakCounter schemas
class StreakCounter(BaseModel):
    streakCount: int
    daysSkipped: int
    currentDayCompleted: bool

class StreakCounterResponse(BaseModel):
    streakCounter: StreakCounter

class StreakCounterRequest(BaseModel):
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

# RecentAcs schemas
class RecentAc(BaseModel):
    id: str
    title: str
    titleSlug: str
    timestamp: str

class RecentAcResponse(BaseModel):
    recentAcSubmissionList: List[RecentAc]

class RecentAcRequest(BaseModel):
    username: str
    limit: int
    leetcodeSession: str = Field(..., description="This is the leetcode cookie, that i will be using for the authentication")

class Language(BaseModel):
    id: str
    name: str
    verboseName: str

class LanguageListResponse(BaseModel):
    languageList: List[Language]