from fastapi import APIRouter, HTTPException
from app.core.graphqlClient import executeQuery
from app.schemas.questionTags import SingleQuestionTopicTagsRequest, SingleQuestionTopicTagsResponse

router = APIRouter()

SINGLE_QUESTION_TOPIC_TAGS_QUERY = """
query singleQuestionTopicTags($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    topicTags {
      name
      slug
    }
  }
}
"""

@router.post("/single-question-topic-tags", response_model=SingleQuestionTopicTagsResponse)
async def get_single_question_topic_tags(request: SingleQuestionTopicTagsRequest):
    variables = {
        "titleSlug": request.titleSlug
    }
    
    result = await executeQuery(SINGLE_QUESTION_TOPIC_TAGS_QUERY, variables)
    
    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"][0]["message"])
    
    return SingleQuestionTopicTagsResponse(**result["data"])