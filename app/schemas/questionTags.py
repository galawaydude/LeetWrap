from pydantic import BaseModel
from typing import List

class TopicTag(BaseModel):
    name: str
    slug: str

class Question(BaseModel):
    topicTags: List[TopicTag]

class SingleQuestionTopicTagsResponse(BaseModel):
    question: Question

class SingleQuestionTopicTagsRequest(BaseModel):
    titleSlug: str