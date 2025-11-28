import re
import unicodedata
from langdetect import detect
from bs4 import BeautifulSoup

def clean_text(text):
	"""
	Advanced cleaning: remove HTML, emojis, special chars, normalize, and detect language.
	Returns cleaned text (English only, else returns None).
	"""
	# Remove HTML tags
	text = BeautifulSoup(text, "html.parser").get_text()
	# Remove emojis and non-ASCII
	text = text.encode('ascii', 'ignore').decode('ascii')
	# Remove special characters
	text = re.sub(r'[^\w\s.,!?]', '', text)
	# Normalize whitespace
	text = unicodedata.normalize('NFKC', text)
	text = re.sub(r'\s+', ' ', text).strip()
	# Language detection (English only)
	try:
		lang = detect(text)
		if lang != 'en':
			return None
	except Exception:
		return None
	return text
