from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.userSessionProgress import UserSessionProgressRequest, UserSessionProgressResponse

router = APIRouter()

USER_SESSION_PROGRESS_QUERY = """
query userSessionProgress($username: String!) {
  allQuestionsCount {
    difficulty
    count
  }
  matchedUser(username: $username) {
    submitStats {
      acSubmissionNum {
        difficulty
        count
        submissions
      }
      totalSubmissionNum {
        difficulty
        count
        submissions
      }
    }
  }
}
"""

@router.post("/user-session-progress", response_model=UserSessionProgressResponse)
async def get_user_session_progress(request: UserSessionProgressRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    variables = {
        "username": request.username
    }
    
    result = await executeQuery(USER_SESSION_PROGRESS_QUERY, variables, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return UserSessionProgressResponse(**result["data"])