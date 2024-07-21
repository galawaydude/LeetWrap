from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import execute_query
from app.schemas import QuestionRequest, QuestionResponse

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

@router.post("/question", response_model=QuestionResponse)
async def get_question(request: QuestionRequest):
    variables = {"titleSlug": request.titleSlug}
    result = await execute_query(QUESTION_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    question_data = result["data"]["question"]
    return QuestionResponse(**question_data)