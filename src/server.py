from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.api import analyze_blog
from src.preprocess import clean_text
from src.summarizer import summarize_one_line
from src.sentiment.train_classical import predict_sentiment

app = FastAPI()

# Allow browser requests from the React dev server (and 127.0.0.1)
# Only enable origins you trust in development/production.
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BlogRequest(BaseModel):
    url: str

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_blog_endpoint(request: BlogRequest):
    """
    Accepts a blog URL and returns summary and sentiment analysis.
    """
    result = analyze_blog(request.url)
    return result

@app.post("/sentiment")
def sentiment_endpoint(request: TextRequest):
    """
    Accepts raw text and returns sentiment analysis result and one-line summary.
    """
    cleaned = clean_text(request.text)
    if not cleaned:
        return {"error": "Text could not be processed or is not in English."}
    sentiment = predict_sentiment(cleaned)
    summary = summarize_one_line(cleaned)
    return {"sentiment": sentiment, "summary": summary}

# For local testing, run: uvicorn src.server:app --reload
