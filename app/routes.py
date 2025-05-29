from fastapi import APIRouter, Query
from typing import Optional
from app.tf_idf import TfidfSearchEngine

router = APIRouter()
engine = TfidfSearchEngine()
engine.build_index()

@router.get("/search")
def search(
  query: str = Query(..., min_length=1),
  testament: Optional[str] = Query(None),
  book: Optional[str] = Query(None),
  chapter: Optional[int] = Query(None),
  top_k: int = Query(5, ge=1)
):
  filters = {
    "testament": testament,
    "book": book,
    "chapter": chapter
  }
  results = engine.query(query, top_k=top_k, filters=filters)
  return results