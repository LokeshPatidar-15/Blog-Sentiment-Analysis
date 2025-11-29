
from src.fetcher import fetch_blog_text
from src.preprocess import clean_text
from src.summarizer import summarize_one_line
from src.sentiment.train_classical import predict_sentiment

def analyze_blog(url):
	"""
	Given a blog URL, returns a dict with 'summary' and 'sentiment'.
	"""
	#  Fetch blog text
	text = fetch_blog_text(url)
	if not text:
		return {"error": "Could not fetch blog content."}

	#  Preprocess text
	cleaned = clean_text(text)
	if not cleaned:
		return {"error": "Blog is not in English or could not be cleaned."}

	#  Summarize
	summary = summarize_one_line(cleaned)

	#  Sentiment analysis
	sentiment = predict_sentiment(cleaned)

	return {"summary": summary, "sentiment": sentiment}

#  uvicorn src.server:app --reload
