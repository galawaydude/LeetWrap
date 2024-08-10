from pydantic import BaseModel, Field

class StreakCounter(BaseModel):
    streakCount: int
    daysSkipped: int
    currentDayCompleted: bool

class StreakCounterResponse(BaseModel):
    streakCounter: StreakCounter

class StreakCounterRequest(BaseModel):
    leetcodeSession: str = Field(..., description="Full cookie string including LEETCODE_SESSION and csrftoken")