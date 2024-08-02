import google.generativeai as genai
import json
from extraction import extract_data
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')

# Configure the Gemini API key
genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_content_with_llm(text):
    prompt = f"Analyze the following text from an article:\n\n{text}\n\nIdentify the main topics, claims, medical terms, conditions and treatments. Give me a clearly formatted response."
    response = model.generate_content(prompt)
    analysis = response.to_dict()  # or extract the necessary fields manually

    # text_part = response.candidates[0]['content']['parts'][0]['text']

    return analysis



def update_json(input_file, output_file):
    # Read the existing JSON data
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Update each article's analysis field to only contain the text subpart
    for article in data:
        if 'analysis' in article:
            # Extract only the 'text' subpart
            article['analysis'] = {
                'text': article['analysis'].get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
            }
    
    # Write the updated data back to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)
    


def main():
    articles = json.loads(extract_data())
    for article in articles:
        analysis = analyze_content_with_llm(article['content'])
        if analysis:
            # print(analysis)
            article['analysis'] = analysis
            
        else:
            print("Failed to analyze content.")
            article['analysis'] = "Failed to analyze content."
        
    
    with open('analyzed_articles.json', 'w') as json_file:
        json.dump(articles, json_file, indent=4)

    update_json('analyzed_articles.json','articles.json')

if __name__ == "__main__":
    main()