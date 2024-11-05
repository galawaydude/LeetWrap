from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

# Base Models
class TopicTag(BaseModel):
    name: str
    id: str
    slug: str

# Question Status Models
class QuestionStatus(BaseModel):
    status: Optional[str]

class UserQuestionStatusRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class UserQuestionStatusResponse(BaseModel):
    question: QuestionStatus

# Basic Question Models
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

# Similar Questions Models
class SimilarQuestion(BaseModel):
    difficulty: str
    titleSlug: str
    title: str
    translatedTitle: Optional[str]
    isPaidOnly: bool

class SimilarQuestionsResponse(BaseModel):
    similarQuestionList: List[SimilarQuestion]

# Daily Challenge Models
class Question(BaseModel):
    acRate: float
    difficulty: str
    freqBar: Optional[float]
    frontendQuestionId: str
    isFavor: bool
    paidOnly: bool
    status: Optional[str]
    title: str
    titleSlug: str
    hasVideoSolution: bool
    hasSolution: bool
    topicTags: List[TopicTag]

class ActiveDailyCodingChallengeQuestion(BaseModel):
    date: str
    userStatus: Optional[str]
    link: str
    question: Question

class QuestionOfTodayResponse(BaseModel):
    activeDailyCodingChallengeQuestion: ActiveDailyCodingChallengeQuestion

# Panel Question Models
class PanelQuestion(BaseModel):
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
    questions: List[PanelQuestion]

class PanelQuestionListRequest(BaseModel):
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class PanelQuestionListResponse(BaseModel):
    panelQuestionList: PanelQuestionList

# Question Stats Models
class QuestionStatsRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class QuestionStatsResponse(BaseModel):
    stats: str

# Question Hints Models
class QuestionHintsRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class QuestionHintsResponse(BaseModel):
    hints: List[str]

# Topic Tags Models
class SingleQuestionTopicTagsRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class SingleQuestionTopicTagsResponse(BaseModel):
    topicTags: List[TopicTag]

# Question Note Models
class QuestionNoteRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class QuestionNoteResponse(BaseModel):
    note: Optional[str]

# Problemset Question List Models
class ProblemsetQuestionListFilters(BaseModel):
    difficulty: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[List[str]] = None
    listId: Optional[str] = None
    searchKeywords: Optional[str] = None

class ProblemsetQuestionListRequest(BaseModel):
    categorySlug: str = ""
    limit: Optional[int] = 50
    skip: int = 0
    filters: Optional[ProblemsetQuestionListFilters] = Field(default_factory=ProblemsetQuestionListFilters)
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class ProblemsetQuestion(BaseModel):
    acRate: float
    difficulty: str
    freqBar: Optional[float]
    frontendQuestionId: str
    isFavor: bool
    paidOnly: bool
    status: Optional[str]
    title: str
    titleSlug: str
    topicTags: List[TopicTag]
    hasSolution: bool
    hasVideoSolution: bool

class ProblemsetQuestionList(BaseModel):
    total: int
    questions: List[ProblemsetQuestion]

class ProblemsetQuestionListResponse(BaseModel):
    problemsetQuestionList: ProblemsetQuestionList
