from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.db import get_all_verses

class TfidfSearchEngine:
  def __init__(self):
    self.verse_metadata = []  # List of dicts with id, book, chapter, verse, text
    self.vectorizer = TfidfVectorizer(stop_words='english')
    self.tfidf_matrix = None

  def build_index(self):
    self.verse_metadata = get_all_verses()
    texts = [verse['text'] for verse in self.verse_metadata]
    self.tfidf_matrix = self.vectorizer.fit_transform(texts)

  def query(self, user_input, top_k=5, filters=None):
    filters = filters or {}
    all_verses = get_all_verses()

    # Apply filters BEFORE indexing
    filtered_verses = []
    for verse in all_verses:
      if filters.get("testament") and verse["testament"].lower() != filters["testament"].lower():
        continue
      if filters.get("book") and verse["book"].lower() != filters["book"].lower():
        continue
      if filters.get("chapter") and verse["chapter"] != filters["chapter"]:
        continue
      filtered_verses.append(verse)

    if not filtered_verses:
      return []

    self.verse_ids = [v["id"] for v in filtered_verses]
    self.texts = [v["text"] for v in filtered_verses]
    self.tfidf_matrix = self.vectorizer.fit_transform(self.texts)

    query_vec = self.vectorizer.transform([user_input])
    similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
    ranked_indices = similarities.argsort()[::-1][:top_k]

    return [
      {
        "id": filtered_verses[i]["id"],
        "book": filtered_verses[i]["book"],
        "chapter": filtered_verses[i]["chapter"],
        "verse": filtered_verses[i]["verse"],
        "text": filtered_verses[i]["text"],
        "testament": filtered_verses[i]["testament"],
        "similarity": float(similarities[i])
      }
      for i in ranked_indices
    ]
