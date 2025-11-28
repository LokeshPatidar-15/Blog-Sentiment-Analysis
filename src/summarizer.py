from transformers import pipeline

_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_one_line(text):
	"""
	Uses BART transformer to generate a one-line summary of the input text.
	Truncates input to 1024 characters to avoid model errors.
	"""
	if not text or len(text.split()) < 20:
		return "Text too short for summarization."
	safe_text = text[:1024]
	result = _summarizer(safe_text, max_length=30, min_length=5, do_sample=False)
	return result[0]["summary_text"].strip()
