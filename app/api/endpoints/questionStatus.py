from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.questionStatus import UserQuestionStatusRequest, UserQuestionStatusResponse

router = APIRouter()

USER_QUESTION_STATUS_QUERY = """
query userQuestionStatus($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    status
  }
}
"""

@router.post("/user-question-status", response_model=UserQuestionStatusResponse)
async def get_user_question_status(request: UserQuestionStatusRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    variables = {
        "titleSlug": request.titleSlug
    }
    
    result = await executeQuery(USER_QUESTION_STATUS_QUERY, variables, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return UserQuestionStatusResponse(**result["data"])