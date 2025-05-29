from fastapi import APIRouter, Query
from app.tf_idf import TfidfSearchEngine

router = APIRouter()
engine = TfidfSearchEngine()
engine.build_index()

@router.get("/search")
def search(query: str = Query(..., min_length=1)):
  results = engine.query(query)
  return [
    {
      "id": verse["id"],
      "book": verse["book"],
      "testament": verse["testament"],
      "chapter": verse["chapter"],
      "verse": verse["verse"],
      "text": verse["text"],
      "similarity": verse["similarity"]
    }
    for verse in results
  ]
