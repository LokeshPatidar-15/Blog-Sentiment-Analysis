# Blog Sentiment & Summary Extractor

This project provides an advanced API to extract the main content from any blog URL, generate a one-line summary, and perform sentiment analysis (positive, negative, neutral) using transformer models.

## Features
- Extracts blog content from a wide variety of sites (WordPress, Blogger, Dev.to, TechCrunch, etc.)
- Uses Selenium for JavaScript-rendered pages
- Generates concise summaries using BART transformer
- Sentiment analysis with RoBERTa (3-class: positive, negative, neutral)
- FastAPI endpoints for easy integration with any frontend

## Setup
1. Clone the repository
2. Install dependencies:
	 ```
	 pip install -r requirements.txt
	 pip install selenium webdriver-manager
	 ```
3. Run the API server:
	 ```
	 uvicorn src.server:app --reload
	 ```

## API Endpoints

### 1. Analyze Blog URL
- **POST** `/analyze`
- **Body:**
	```json
	{ "url": "https://blog.example.com/post-url" }
	```
- **Response:**
	```json
	{
		"summary": "One-line summary of the blog post.",
		"sentiment": { "label": "positive", "score": 0.98 }
	}
	```

### 2. Sentiment & Summary for Raw Text
- **POST** `/sentiment`
- **Body:**
	```json
	{ "text": "Your text here." }
	```
- **Response:**
	```json
	{
		"sentiment": { "label": "neutral", "score": 0.52 },
		"summary": "One-line summary of the text."
	}
	```

## Troubleshooting
- If you get `Could not fetch blog content`, check:
	- The blog URL is valid and public
	- The site is not protected by login, paywall, or bot detection
	- Selenium and ChromeDriver are installed and working
- For JavaScript-heavy sites, Selenium will be used automatically
- Check logs for `[Requests]` and `[Selenium]` messages for extraction details

## Example Test URLs
- https://martinfowler.com/bliki/UnitTest.html
- https://dev.to/ben/the-dev-community-is-growing-1p7n
- https://blog.python.org/2025/10/python-3140-final-is-here.html

## License
MIT
