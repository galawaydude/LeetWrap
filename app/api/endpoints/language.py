from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.language import LanguageListResponse

router = APIRouter()

LANGUAGE_LIST_QUERY = """
query languageList {
  languageList {
    id
    name
  }
}
"""

@router.get("/languages", response_model=LanguageListResponse)
async def get_language_list():
    result = await executeQuery(LANGUAGE_LIST_QUERY, {})
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return LanguageListResponse(**result["data"])