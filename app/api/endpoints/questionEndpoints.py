from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.question import QuestionRequest, QuestionResponse, SimilarQuestionsResponse
from app.schemas.questionStats import QuestionStatsRequest, QuestionStatsResponse
from app.schemas.getQuestionHints import QuestionHintsRequest, QuestionHintsResponse
from app.schemas.questionTags import SingleQuestionTopicTagsRequest, SingleQuestionTopicTagsResponse
from app.schemas.questionNote import QuestionNoteRequest, QuestionNoteResponse
from app.schemas.questionStatus import UserQuestionStatusRequest, UserQuestionStatusResponse

router = APIRouter()

# Query strings
QUESTION_QUERY = """
query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    isPaidOnly
    difficulty
    likes
    dislikes
    content
  }
}
"""

SIMILAR_QUESTIONS_QUERY = """
query SimilarQuestions($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    similarQuestionList {
      difficulty
      titleSlug
      title
      translatedTitle
      isPaidOnly
    }
  }
}
"""

QUESTION_STATS_QUERY = """
query questionStats($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    stats
  }
}
"""

QUESTION_HINTS_QUERY = """
query questionHints($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    hints
  }
}
"""

SINGLE_QUESTION_TOPIC_TAGS_QUERY = """
query singleQuestionTopicTags($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    topicTags {
      name
      slug
    }
  }
}
"""

QUESTION_NOTE_QUERY = """
query questionNote($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    note
  }
}
"""

USER_QUESTION_STATUS_QUERY = """
query userQuestionStatus($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    status
  }
}
"""

# Endpoints
@router.post("/question", response_model=QuestionResponse)
async def get_question(request: QuestionRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(QUESTION_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    questionData = result["data"]["question"]
    return QuestionResponse(**questionData)

@router.post("/similar-questions", response_model=SimilarQuestionsResponse)
async def get_similar_questions(request: QuestionRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(SIMILAR_QUESTIONS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    payload = result["data"]["question"]
    return SimilarQuestionsResponse(**payload)

@router.post("/question-stats", response_model=QuestionStatsResponse)
async def get_question_stats(request: QuestionStatsRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(QUESTION_STATS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return QuestionStatsResponse(**result["data"])

@router.post("/question-hints", response_model=QuestionHintsResponse)
async def get_question_hints(request: QuestionHintsRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(QUESTION_HINTS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return QuestionHintsResponse(**result["data"])

@router.post("/question-topic-tags", response_model=SingleQuestionTopicTagsResponse)
async def get_question_topic_tags(request: SingleQuestionTopicTagsRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(SINGLE_QUESTION_TOPIC_TAGS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return SingleQuestionTopicTagsResponse(**result["data"])

@router.post("/question-note", response_model=QuestionNoteResponse)
async def get_question_note(request: QuestionNoteRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(QUESTION_NOTE_QUERY, variables, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return QuestionNoteResponse(**result["data"])

@router.post("/question-status", response_model=UserQuestionStatusResponse)
async def get_question_status(request: UserQuestionStatusRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(USER_QUESTION_STATUS_QUERY, variables, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return UserQuestionStatusResponse(**result["data"])