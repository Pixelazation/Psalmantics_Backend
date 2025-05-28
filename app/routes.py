from fastapi import APIRouter, Query
from app.api_client import fetch_verse
from app.td_idf import search_corpus

router = APIRouter()

@router.get("/verse")
async def get_verse(
    version: str = Query(...), 
    book: str = Query(...), 
    chapter: str = Query(...), 
    verse: str = Query(...)
):
    return await fetch_verse(version, book, chapter, verse)

@router.get("/search")
def search(q: str = Query(...)):
    return search_corpus(q)
