from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.userFavorites import UserFavoritesRequest, UserFavoritesResponse

router = APIRouter()

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