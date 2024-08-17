from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.questionSchemas import QuestionOfTodayResponse
from app.schemas.userSchemas import StreakCounterRequest, StreakCounterResponse
from app.schemas.userSchemas import LanguageListResponse

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

STREAK_COUNTER_QUERY = """
query getStreakCounter {
  streakCounter {
    streakCount
    daysSkipped
    currentDayCompleted
  }
}
"""

LANGUAGE_LIST_QUERY = """
query languageList {
  languageList {
    id
    name
    verboseName
  }
}
"""

@router.get("/question-of-today", response_model=QuestionOfTodayResponse)
async def get_question_of_today():
    result = await executeQuery(QUESTION_OF_TODAY_QUERY)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return QuestionOfTodayResponse(**result["data"])

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

@router.get("/language-list", response_model=LanguageListResponse)
async def get_language_list():
    result = await executeQuery(LANGUAGE_LIST_QUERY)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return LanguageListResponse(**result["data"])