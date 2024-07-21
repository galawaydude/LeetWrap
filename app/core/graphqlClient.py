import httpx
from app.core.config import settings

async def execute_query(query: str, variables: dict, custom_headers: dict = None):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    if custom_headers:
        headers.update(custom_headers)

    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.LEETCODE_API_URL,
            json={"query": query, "variables": variables},
            headers=headers
        )
        response.raise_for_status()
        return response.json()