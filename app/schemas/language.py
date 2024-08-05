from pydantic import BaseModel
from typing import List

class Language(BaseModel):
    id: int
    name: str

class LanguageListResponse(BaseModel):
    languageList: List[Language]
    