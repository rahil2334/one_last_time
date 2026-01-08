from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class IdeaAnalysisEngine:
    def __init__(self, dataset_texts):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.dataset_vectors = self.vectorizer.fit_transform(dataset_texts)

    def analyze_idea(self, user_idea):
        user_vector = self.vectorizer.transform([user_idea])
        similarity = cosine_similarity(user_vector, self.dataset_vectors)[0]

        confidence = float(np.mean(similarity) * 100)

        return {
            "confidence_score": round(confidence, 2),
            "risk_level": "LOW" if confidence > 70 else "MEDIUM" if confidence > 40 else "HIGH"
        }
