from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
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
async def getQuestionStats(request: StatsRequest):
    variables = {"titleSlug": request.titleSlug}
    
    result = await executeQuery(STATS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    payload = result["data"]["question"]
    return StatsResponse(**payload)