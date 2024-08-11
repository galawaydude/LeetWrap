from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.questionNote import QuestionNoteRequest, QuestionNoteResponse

router = APIRouter()

QUESTION_NOTE_QUERY = """
query questionNote($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    note
  }
}
"""

@router.post("/question-note", response_model=QuestionNoteResponse)
async def get_question_note(request: QuestionNoteRequest):
    headers = {
        "Cookie": request.leetcodeSession,
        "Referer": "https://leetcode.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    variables = {
        "titleSlug": request.titleSlug
    }
    
    result = await executeQuery(QUESTION_NOTE_QUERY, variables, customHeaders=headers)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return QuestionNoteResponse(**result["data"])