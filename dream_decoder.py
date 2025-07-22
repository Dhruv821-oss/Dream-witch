import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class DreamDecoder:
    def __init__(self, csv_path="dreams_interpretations.csv", model_name="all-MiniLM-L6-v2"):
        self.df = pd.read_csv(csv_path)
        self.texts = (self.df["Dream Symbol"] + ": " + self.df["Interpretation"]).tolist()
        self.model = SentenceTransformer(model_name, device='cpu')  # Safe on PyTorch 2.3+
        self.embeddings = self.model.encode(self.texts)

    def decode(self, user_dream, top_k=3):
        user_embedding = self.model.encode([user_dream])
        similarities = cosine_similarity(user_embedding, self.embeddings)[0]
        top_indices = similarities.argsort()[-top_k:][::-1]

        return [
            {
                "symbol": self.df["Dream Symbol"][i],
                "interpretation": self.df["Interpretation"][i],
                "similarity": float(similarities[i])
            }
            for i in top_indices
        ]
