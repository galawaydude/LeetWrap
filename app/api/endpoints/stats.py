from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import execute_query
from app.schemas.stats import StatsRequest, StatsResponse

router = APIRouter()

STATS_QUERY = """
query questionStats($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    stats
  }
}
"""

@router.post("/stats", response_model=StatsResponse)
async def get_question_stats(request: StatsRequest):
    variables = {"titleSlug": request.titleSlug}
    
    result = await execute_query(STATS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    stats_data = result["data"]["question"]
    return StatsResponse(**stats_data)