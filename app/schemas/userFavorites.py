from pydantic import BaseModel, Field
from typing import List

class Question(BaseModel):
    titleSlug: str

class Favorite(BaseModel):
    idHash: str
    name: str
    isPublicFavorite: bool
    questions: List[Question]

class FavoritesList(BaseModel):
    allFavorites: List[Favorite]

class UserFavoritesResponse(BaseModel):
    favoritesLists: FavoritesList

class UserFavoritesRequest(BaseModel):
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")