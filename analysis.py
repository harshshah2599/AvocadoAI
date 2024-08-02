import google.generativeai as genai
import json
from extraction import extract_data
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')

# Ensure API key is loaded
if not api_key:
    raise ValueError("API_KEY is not set in environment variables.")

# Configure the Gemini API key
genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_content_with_llm(text):
    """
    Analyzes the content using the Gemini model and returns the structured analysis.
    
    Args:
        text (str): The text content to analyze.
    
    Returns:
        dict: The analysis response from the model.
    """
    prompt = (f"Analyze the following text from an article:\n\n{text}\n\n"
              "Identify the main topics, claims, medical terms, conditions, and treatments. "
              "Provide a clearly formatted response.")
    
    response = model.generate_content(prompt)
    # Convert response to dictionary format
    analysis = response.to_dict()  

    return analysis

def update_json(input_file, output_file):
    """
    Updates the JSON file by extracting the 'text' subpart from the 'analysis' field.
    
    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to the output JSON file.
    """
    # Read the existing JSON data
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Update each article's 'analysis' field
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
    """
    Main function to extract data, analyze it, and update the JSON files.
    """
    articles = json.loads(extract_data())
    
    # Analyze each article and update the 'analysis' field
    for article in articles:
        analysis = analyze_content_with_llm(article['content'])
        if analysis:
            article['analysis'] = analysis
        else:
            print("Failed to analyze content.")
            article['analysis'] = "Failed to analyze content."
    
    # Save analyzed articles to a JSON file
    with open('analyzed_articles.json', 'w') as json_file:
        json.dump(articles, json_file, indent=4)

    # Update the original JSON file with extracted 'text' subpart
    update_json('analyzed_articles.json', 'articles.json')

if __name__ == "__main__":
    main()