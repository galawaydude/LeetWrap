from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.QOTD import QuestionOfTodayResponse

router = APIRouter()

QUESTION_OF_TODAY_QUERY = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    userStatus
    link
    question {
      acRate
      difficulty
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      paidOnly: isPaidOnly
      status
      title
      titleSlug
      hasVideoSolution
      hasSolution
      topicTags {
        name
        id
        slug
      }
    }
  }
}
"""

@router.get("/question-of-today", response_model=QuestionOfTodayResponse)
async def get_question_of_today():
    result = await executeQuery(QUESTION_OF_TODAY_QUERY)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return QuestionOfTodayResponse(**result["data"])