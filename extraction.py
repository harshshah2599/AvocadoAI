import requests
from bs4 import BeautifulSoup
import json
import random
import numpy as np

def extract_data():
    full_urls = get_article_links()
    combined_data = []
    for link in full_urls:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.find('h1').text if soup.find('h1') else 'No Title Found'
        url = link

        published_div = soup.find('div', class_='flo-article-banner-bottom__info-panel-date')
        date = ""
        if published_div:
            published_items = published_div.find_all('div', class_='flo-article-banner-bottom__info-panel-date--item')
            for item in published_items:
                if 'Published' in item.text:
                    date = item.find('span').text.strip()
                    break
                
        paragraphs = soup.find_all('p')
        content = " ".join([para.get_text() for para in paragraphs])
        
        data = {
            'title': title,
            'url': url,
            'date': date,
            'content': content
        }
        combined_data.append(data)
    
    return json.dumps(combined_data, indent=2)

def get_article_links():
    base_url = "https://flo.health/menstrual-cycle/health"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find_all(class_='flo-section flo-category-headling')
    headings = [a['href'] for heading in categories for a in heading.find_all('a')]
    
    selected_category = np.random.choice(headings, 1, replace=False)[0]
    selected_category = selected_category.replace('#', '')

    api_url = f"{base_url}/{selected_category}?page=1&format=json&onpage=8"
    api_response = requests.get(api_url)

    if api_response.status_code == 200:
        data = api_response.json()
        articles = data.get('items', [])
        links = [article.get('link') for article in articles]
        random_links = random.sample(links, min(5, len(links)))
        full_urls = [f"https://flo.health{link}" for link in random_links]

        return full_urls

if __name__ == "__main__":
    extract_data()