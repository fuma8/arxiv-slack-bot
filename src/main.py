import os

from dotenv import load_dotenv
import requests

from embedding_service import EmbeddingService
from arxiv_client import ArxivClient

load_dotenv()
huggingface_token = os.getenv("HUGGINGFACE_TOKEN")

def main():
    query = "diffusion model"  # 興味のある分野のクエリ
    max_papers = 10                           # 取得する最大論文数

    # arXivクライアントと埋め込みサービスを初期化
    arxiv_client = ArxivClient(max_results=max_papers)
    embedding_service = EmbeddingService(huggingface_token=huggingface_token)

    # arXivから論文データを取得
    xml_data = arxiv_client.get_papers(query)
    papers = arxiv_client.parse_papers(xml_data)
    
    # クエリと各論文の類似度を計算し、ソート
    sorted_papers = embedding_service.embed_papers(query, papers)
    
    # 結果を表示
    print("Top relevant papers:")
    for result in sorted_papers:
        paper = result["paper"]
        print(f"Title: {paper['title']}")
        print(f"Link: {paper['link']}")
        print(f"Similarity: {result['similarity']:.4f}\n")

    
if __name__ == "__main__":
    main()