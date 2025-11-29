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

	text = text.encode('ascii', 'ignore').decode('ascii')

	text = re.sub(r'[^\w\s.,!?]', '', text)

	text = unicodedata.normalize('NFKC', text)
	text = re.sub(r'\s+', ' ', text).strip()
	
	try:
		lang = detect(text)
		if lang != 'en':
			return None
	except Exception:
		return None
	return text
