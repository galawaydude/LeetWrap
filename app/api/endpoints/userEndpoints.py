from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.userFavorites import UserFavoritesRequest, UserFavoritesResponse
from app.schemas.userSessionProgress import UserSessionProgressRequest, UserSessionProgressResponse
from app.schemas.getStreakCounter import StreakCounterRequest, StreakCounterResponse
from app.schemas.recentAcs import recentAcResponse, recentAcRequest
from app.schemas.userPublicProfile import UserPublicProfileRequest, UserPublicProfileResponse

router = APIRouter()

# Query strings
USER_FAVORITES_QUERY = """
query userFavorites {
  favoritesLists {
    allFavorites {
      idHash
      name
      isPublicFavorite
      questions {
        titleSlug
      }
    }
  }
}
"""

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

STREAK_COUNTER_QUERY = """
query getStreakCounter {
  streakCounter {
    streakCount
    daysSkipped
    currentDayCompleted
  }
}
"""

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

USER_PUBLIC_PROFILE_QUERY = """
query userPublicProfile($username: String!) {
  matchedUser(username: $username) {
    contestBadge {
      name
      expired
      hoverText
      icon
    }
    username
    githubUrl
    twitterUrl
    linkedinUrl
    profile {
      ranking
      userAvatar
      realName
      aboutMe
      school
      websites
      countryName
      company
      jobTitle
      skillTags
      postViewCount
      postViewCountDiff
      reputation
      reputationDiff
      solutionCount
      solutionCountDiff
      categoryDiscussCount
      categoryDiscussCountDiff
    }
  }
}
"""

# Endpoints
@router.post("/user-favorites", response_model=UserFavoritesResponse)
async def get_user_favorites(request: UserFavoritesRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    result = await executeQuery(USER_FAVORITES_QUERY, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return UserFavoritesResponse(**result["data"])

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

@router.post("/recent-ac", response_model=recentAcResponse)
async def get_recent_ac(request: recentAcRequest):
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

@router.post("/user-public-profile", response_model=UserPublicProfileResponse)
async def get_user_public_profile(request: UserPublicProfileRequest):
    variables = {
        "username": request.username
    }

    result = await executeQuery(USER_PUBLIC_PROFILE_QUERY, variables)

    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return UserPublicProfileResponse(**result["data"])