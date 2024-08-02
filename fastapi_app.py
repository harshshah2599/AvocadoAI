from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import uvicorn

from analysis import analyze_content_with_llm

app = FastAPI()

class Article(BaseModel):
    """
    Data model for the article input.
    
    Attributes:
    - text (str): The content of the article to be analyzed.
    - other_field (int): An additional field for demonstration purposes.
    """
    text: str
    other_field: int

@app.post("/analyze")
def analyze_article(article: Article):
    """
    Endpoint to analyze the content of an article.
    
    Args:
    - article (Article): The article data containing text and other_field.

    Returns:
    - dict: A dictionary containing the analysis result.

    Raises:
    - HTTPException: If an error occurs during the analysis process.
    """
    try:
        # Perform content analysis using the provided function
        analysis = analyze_content_with_llm(article.text)
        return {"analysis": str(analysis)}
    except Exception as e:
        # Log the exception and return a 500 error response
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Run the FastAPI application using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)