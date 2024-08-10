from pydantic import BaseModel
from typing import List, Optional

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