from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    LEETCODE_API_URL: str = "https://leetcode.com/graphql"
settings = Settings()