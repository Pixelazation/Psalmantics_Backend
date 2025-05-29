import httpx
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

API_KEY = os.getenv("BIBLE_API_KEY")
BASE_URL = "https://api.scripture.api.bible/v1"

HEADERS = {"api-key": API_KEY}

async def fetch_verse(version: str, book: str, chapter: str, verse: str):
    url = f"{BASE_URL}/bibles/{version}/verses/{book}.{chapter}.{verse}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
