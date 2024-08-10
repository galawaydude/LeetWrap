from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.getStreakCounter import StreakCounterRequest, StreakCounterResponse

router = APIRouter()

STREAK_COUNTER_QUERY = """
query getStreakCounter {
  streakCounter {
    streakCount
    daysSkipped
    currentDayCompleted
  }
}
"""

@router.post("/streak-counter", response_model=StreakCounterResponse)
async def get_streak_counter(request: StreakCounterRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    result = await executeQuery(STREAK_COUNTER_QUERY, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return StreakCounterResponse(**result["data"])