from pydantic import BaseModel

class StatsRequest(BaseModel):
    titleSlug: str

class StatsResponse(BaseModel):
    stats: str