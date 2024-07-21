from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import execute_query
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
async def get_question(request: QuestionRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await execute_query(QUESTION_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    question_data = result["data"]["question"]
    return QuestionResponse(**question_data)

@router.post("/similar-questions", response_model=SimilarQuestionsResponse)
async def get_similar_questions(request: QuestionRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await execute_query(SIMILAR_QUESTIONS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    similar_questions_data = result["data"]["question"]
    return SimilarQuestionsResponse(**similar_questions_data)