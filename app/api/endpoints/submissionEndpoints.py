from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.submissionSchemas import (
    SubmissionListRequest, SubmissionListResponse,
    SubmissionDetailsRequest, SubmissionDetailsResponse
)
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

SUBMISSION_DETAILS_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    runtime
    runtimeDisplay
    runtimePercentile
    runtimeDistribution
    memory
    memoryDisplay
    memoryPercentile
    memoryDistribution
    code
    timestamp
    statusCode
    user {
      username
      profile {
        realName
        userAvatar
      }
    }
    lang {
      name
      verboseName
    }
    question {
      questionId
    }
    notes
    topicTags {
      tagId
      slug
      name
    }
    runtimeError
    compileError
    lastTestcase
  }
}
"""

@router.post("/submission-list", response_model=SubmissionListResponse)
async def get_submission_list(request: SubmissionListRequest):
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

@router.post("/submission-details", response_model=SubmissionDetailsResponse)
async def get_submission_details(request: SubmissionDetailsRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    variables = {
        "submissionId": request.submissionId
    }
    
    result = await executeQuery(SUBMISSION_DETAILS_QUERY, variables, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return SubmissionDetailsResponse(**result["data"])