from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.recentAcs import recentAcResponse, recentAcRequest

router = APIRouter()

RECENT_AC_QUERY = """
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    id
    title
    titleSlug
    timestamp
  }
}
"""

@router.post("/recentAc", response_model=recentAcResponse)
async def getRecentAc(request: recentAcRequest):
    print("Shit")
    variables = {
        "username": request.username, 
        "limit": request.limit
    }

    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }


    result = await executeQuery(RECENT_AC_QUERY, variables, customHeaders=headers)

    if "errors" in result: 
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    payload = result["data"]
    return recentAcResponse(**payload)
    
