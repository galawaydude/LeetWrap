from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    LEETCODE_API_URL: str = "https://leetcode.com/graphql"
    LEETCODE_SESSION: str = os.getenv("LEETCODE_SESSION")
    CSRF_TOKEN: str = os.getenv("CSRF_TOKEN")

settings = Settings()