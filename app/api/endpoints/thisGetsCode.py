from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.thisGetsCode import SubmissionDetailsRequest, SubmissionDetailsResponse

router = APIRouter()

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