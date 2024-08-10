from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.getQuestionHints import QuestionHintsRequest, QuestionHintsResponse

router = APIRouter()

QUESTION_HINTS_QUERY = """
query questionHints($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    hints
  }
}
"""

@router.post("/question-hints", response_model=QuestionHintsResponse)
async def get_question_hints(request: QuestionHintsRequest):
    variables = {
        "titleSlug": request.titleSlug
    }
    
    result = await executeQuery(QUESTION_HINTS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return QuestionHintsResponse(**result["data"])