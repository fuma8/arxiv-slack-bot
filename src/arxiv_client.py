import requests
import xml.etree.ElementTree as ET

class ArxivClient:
    BASE_URL = "http://export.arxiv.org/api/query"
    
    def __init__(self, max_results=10):
        self.max_results = max_results
        
    def get_papers(self, query):
        url = f'{self.BASE_URL}?search_query={query}&start=0&max_results={self.max_results}'
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def parse_papers(self, xml_data):
        root = ET.fromstring(xml_data)
        papers = []
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
            link = entry.find('{http://www.w3.org/2005/Atom}id').text
            papers.append({"title": title, "summary": summary, "link": link})
        return papers