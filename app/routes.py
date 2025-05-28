from fastapi import APIRouter, Query
from app.api_client import BibleAPIClient
from app.tf_idf import VerseSearchEngine

router = APIRouter()

# Example: a small verse corpus for demo purposes
VERSE_CORPUS = [
    "For God so loved the world that he gave his one and only Son.",
    "The Lord is my shepherd; I shall not want.",
    "In the beginning God created the heavens and the earth.",
    "I can do all things through Christ who strengthens me.",
    "Trust in the Lord with all your heart and lean not on your own understanding."
]
VERSE_REFERENCES = [
    "John 3:16",
    "Psalm 23:1",
    "Genesis 1:1",
    "Philippians 4:13",
    "Proverbs 3:5"
]
search_engine = VerseSearchEngine(VERSE_CORPUS)

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/verse/")
async def get_verse(reference: str = Query(..., description="e.g. John 3:16")):
    """
    Fetch a verse from the Bible API.
    """
    return BibleAPIClient.get_verse(reference)

@router.get("/search/")
async def search_verses(query: str = Query(..., description="Search query"), top_k: int = 3):
    """
    Search the local verse corpus using TF-IDF.
    """
    results = search_engine.search(query, top_k)
    return [
        {"reference": VERSE_REFERENCES[idx], "verse": VERSE_CORPUS[idx], "score": float(score)}
        for idx, score in results
    ]
