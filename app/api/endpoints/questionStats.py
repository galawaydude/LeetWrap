from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.questionStats import QuestionStatsRequest, QuestionStatsResponse

router = APIRouter()

QUESTION_STATS_QUERY = """
query questionStats($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    stats
  }
}
"""

@router.post("/question-stats", response_model=QuestionStatsResponse)
async def get_question_stats(request: QuestionStatsRequest):
    variables = {
        "titleSlug": request.titleSlug
    }
    
    result = await executeQuery(QUESTION_STATS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return QuestionStatsResponse(**result["data"])