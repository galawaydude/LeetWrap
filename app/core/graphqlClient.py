import httpx
from app.core.config import settings

async def execute_query(query: str, variables: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.LEETCODE_API_URL,
            json={"query": query, "variables": variables},
        )
        response.raise_for_status()
        return response.json()