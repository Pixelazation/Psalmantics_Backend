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

  def query(self, user_input, top_k=5):
    query_vec = self.vectorizer.transform([user_input])
    similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
    ranked_indices = similarities.argsort()[::-1][:top_k]

    results = []
    for i in ranked_indices:
      verse = self.verse_metadata[i]
      results.append({
        'id': verse['id'],
        'book': verse['book'],
        'testament': verse['testament'],
        'chapter': verse['chapter'],
        'verse': verse['verse'],
        'text': verse['text'],
        'similarity': similarities[i]
      })
    return results
