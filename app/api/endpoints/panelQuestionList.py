from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.panelQuestionList import PanelQuestionListRequest, PanelQuestionListResponse

router = APIRouter()

PANEL_QUESTION_LIST_QUERY = """
query panelQuestionList($currentQuestionSlug: String!, $categorySlug: String, $envId: String, $envType: String, $filters: QuestionListFilterInput) {
  panelQuestionList(
    currentQuestionSlug: $currentQuestionSlug
    categorySlug: $categorySlug
    envId: $envId
    envType: $envType
    filters: $filters
  ) {
    hasViewPermission
    panelName
    finishedLength
    totalLength
    questions {
      difficulty
      id
      paidOnly
      questionFrontendId
      status
      title
      titleSlug
      topicTags {
        name
        slug
      }
      score
      questionNumber
    }
  }
}
"""

@router.post("/panel-question-list", response_model=PanelQuestionListResponse)
async def get_panel_question_list(request: PanelQuestionListRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    variables = {
        "currentQuestionSlug": "4sum",
        "categorySlug": None,
        "envId": None,
        "envType": None,
        "filters": None
    }
    
    result = await executeQuery(PANEL_QUESTION_LIST_QUERY, variables, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return PanelQuestionListResponse(panelQuestionList=result["data"]["panelQuestionList"])