from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class VerseSearchEngine:
    def __init__(self, verses: list[str]):
        self.verses = verses
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(verses)

    def search(self, query: str, top_k: int = 3) -> list[tuple[int, float]]:
        """
        Returns indices and scores of top_k most relevant verses.
        """
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = np.argsort(similarities)[::-1][:top_k]
        return [(idx, similarities[idx]) for idx in top_indices if similarities[idx] > 0]