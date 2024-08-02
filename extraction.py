import requests
from bs4 import BeautifulSoup
import json
import random
import numpy as np

def extract_data():
    """
    Extracts data from articles obtained via links.
    """
    # Retrieve article links
    article_links = get_article_links()
    
    # List to store data for all articles
    combined_data = []

    for link in article_links:
        # Fetch and parse the article page
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title
        title = soup.find('h1').text if soup.find('h1') else 'No Title Found'
        
        # Extract the publication date
        date = extract_date(soup)
        
        # Extract the content
        content = " ".join(para.get_text() for para in soup.find_all('p'))
        
        # Create a dictionary for the article data
        article_data = {
            'title': title,
            'url': link,
            'date': date,
            'content': content
        }
        combined_data.append(article_data)
    
    # Return the combined data as a JSON formatted string
    return json.dumps(combined_data, indent=2)

def extract_date(soup):
    """
    Extracts the publication date from the article soup.
    """
    published_div = soup.find('div', class_='flo-article-banner-bottom__info-panel-date')
    if published_div:
        published_items = published_div.find_all('div', class_='flo-article-banner-bottom__info-panel-date--item')
        for item in published_items:
            if 'Published' in item.text:
                return item.find('span').text.strip()
    return "No Date Found"

def get_article_links():
    """
    Retrieves and returns a list of article links.
    """
    base_url = "https://flo.health/menstrual-cycle/health"
    
    # Fetch and parse the main page
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find category links
    categories = soup.find_all(class_='flo-section flo-category-headling')
    headings = [a['href'] for heading in categories for a in heading.find_all('a')]
    
    # Randomly select a category
    selected_category = np.random.choice(headings, 1, replace=False)[0]
    selected_category = selected_category.replace('#', '')

    # Construct API URL and fetch data
    api_url = f"{base_url}/{selected_category}?page=1&format=json&onpage=8"
    api_response = requests.get(api_url)
    
    if api_response.status_code == 200:
        data = api_response.json()
        articles = data.get('items', [])
        links = [article.get('link') for article in articles]
        
        # Randomly select up to 5 article links
        random_links = random.sample(links, min(5, len(links)))
        full_urls = [f"https://flo.health{link}" for link in random_links]
        
        return full_urls

if __name__ == "__main__":
    # Print the extracted data
    extract_data()