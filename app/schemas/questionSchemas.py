from pydantic import BaseModel, Field
from typing import List, Optional

class QuestionStatus(BaseModel):
    status: Optional[str]

class UserQuestionStatusResponse(BaseModel):
    question: QuestionStatus

class UserQuestionStatusRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

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

class SimilarQuestion(BaseModel):
    difficulty: str
    titleSlug: str
    title: str
    translatedTitle: Optional[str]
    isPaidOnly: bool

class SimilarQuestionsResponse(BaseModel):
    similarQuestionList: List[SimilarQuestion]

class TopicTag(BaseModel):
    name: str
    id: str
    slug: str

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

class PanelQuestionListResponse(BaseModel):
    panelQuestionList: PanelQuestionList

class PanelQuestionListRequest(BaseModel):
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

    
class QuestionStatsRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class QuestionStatsResponse(BaseModel):
    stats: str

class QuestionHintsRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class QuestionHintsResponse(BaseModel):
    hints: List[str]

class SingleQuestionTopicTagsRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class SingleQuestionTopicTagsResponse(BaseModel):
    topicTags: List[TopicTag]

class QuestionNoteRequest(BaseModel):
    titleSlug: str
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")

class QuestionNoteResponse(BaseModel):
    note: Optional[str]