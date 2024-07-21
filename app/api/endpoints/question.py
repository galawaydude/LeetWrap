from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.question import QuestionRequest, QuestionResponse, SimilarQuestionsResponse

router = APIRouter()

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

@router.post("/question", response_model=QuestionResponse)
async def getQuestion(request: QuestionRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(QUESTION_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    questionData = result["data"]["question"]
    return QuestionResponse(**questionData)

@router.post("/similarQuestions", response_model=SimilarQuestionsResponse)
async def getSimilarQuestions(request: QuestionRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await executeQuery(SIMILAR_QUESTIONS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    payload = result["data"]["question"]
    return SimilarQuestionsResponse(**payload)