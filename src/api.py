
from src.fetcher import fetch_blog_text
from src.preprocess import clean_text
from src.summarizer import summarize_one_line
from src.sentiment.train_classical import predict_sentiment

def analyze_blog(url):
	"""
	Given a blog URL, returns a dict with 'summary' and 'sentiment'.
	"""
	# Step 1: Fetch blog text
	text = fetch_blog_text(url)
	if not text:
		return {"error": "Could not fetch blog content."}

	# Step 2: Preprocess text
	cleaned = clean_text(text)
	if not cleaned:
		return {"error": "Blog is not in English or could not be cleaned."}

	# Step 3: Summarize
	summary = summarize_one_line(cleaned)

	# Step 4: Sentiment analysis
	sentiment = predict_sentiment(cleaned)

	return {"summary": summary, "sentiment": sentiment}
