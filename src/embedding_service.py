import numpy as np
from transformers import AutoModel

class EmbeddingService:
    def __init__(self, huggingface_token, model_name='jinaai/jina-embeddings-v3'):
        self.model_name = model_name
        self.huggingface_token = huggingface_token
        self.model = AutoModel.from_pretrained(self.model_name, trust_remote_code=True, token=huggingface_token)
    
    def init_embed(self, text):
        """Jina embeddingモデルの初期化"""
        return self.model.encode(text, task="text-matching")
    
    def calculate_similarity(self, query_embedding, text_embeddings):
        similarities = [
            {"paper": paper, "similarity": query_embedding@text_embedding.T}
            for paper, text_embedding in text_embeddings
        ]
        return sorted(similarities, key=lambda x: x['similarity'], reverse=True)

    def embed_papers(self, query, papers):
        """論文のサマリをembeddingし、クエリとの類似度でソート"""
        query_embedding = self.init_embed(query)
        paper_embeddings = [(paper, self.init_embed(paper['summary'])) for paper in papers]
        return self.calculate_similarity(query_embedding, paper_embeddings)