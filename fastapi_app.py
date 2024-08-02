from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from analysis import analyze_content_with_llm

app = FastAPI()

class Article(BaseModel):
    text: str
    other_field: int

@app.post("/analyze")
def analyze_article(article: Article):
    try:
        analysis = analyze_content_with_llm(article.text)
        return {"analysis": str(analysis)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)