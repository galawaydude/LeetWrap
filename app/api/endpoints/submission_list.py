from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.submission_list import SubmissionListRequest, SubmissionListResponse

router = APIRouter()

SUBMISSION_LIST_QUERY = """
query questionSubmissionList($questionSlug: String!, $limit: Int!, $offset: Int!) {
  questionSubmissionList(questionSlug: $questionSlug, limit: $limit, offset: $offset) {
    lastKey
    hasNext
    submissions {
      runtime
      memory
      timestamp
      status
      statusDisplay
      lang
      langName
      notes
      id
      hasNotes
      topicTags {
        id
        name
        slug
        translatedName
      }
    }
  }
}
"""

@router.post("/submissionList", response_model=SubmissionListResponse)
async def getSubmissionList(request: SubmissionListRequest):
    variables = {
        "questionSlug": request.questionSlug,
        "limit": request.limit,
        "offset": request.offset
    }
    
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    result = await executeQuery(SUBMISSION_LIST_QUERY, variables, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    payload = result["data"]["questionSubmissionList"]
    return SubmissionListResponse(**payload)