from transformers import pipeline

# Use a 3-class sentiment model
_sentiment = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

def predict_sentiment(text):
    """
    Uses RoBERTa to predict sentiment (positive/negative/neutral) of the input text.
    Returns label and score.
    """
    if not text or len(text.split()) < 5:
        return {"label": "neutral", "score": 0.0}
    result = _sentiment(text[:512])  # Truncate for model input
    label = result[0]["label"].lower()
    score = float(result[0]["score"])
    return {"label": label, "score": score}
