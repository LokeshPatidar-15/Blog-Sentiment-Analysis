
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging

def extract_text_from_soup(soup):
	text_blocks = []
	for tag in ['article', 'main', 'section']:
		block = soup.find(tag)
		if block:
			text_blocks.append(block.get_text(separator=' ', strip=True))
	for div in soup.find_all('div'):
		if div.get('class') and any(c in div.get('class') for c in ['post', 'content', 'entry', 'article', 'blog']):
			text_blocks.append(div.get_text(separator=' ', strip=True))
	paragraphs = soup.find_all('p')
	if paragraphs:
		text_blocks.append(' '.join(p.get_text(strip=True) for p in paragraphs))
	text = ' '.join(text_blocks)
	text = text.strip()
	return text

def fetch_blog_text(url):
	"""
	Fetches and extracts main text content from a blog URL.
	Returns plain text or None if failed or not enough content.
	Tries requests/BeautifulSoup first, then Selenium if needed.
	Logs extraction attempts for debugging.
	"""
	logging.basicConfig(level=logging.INFO)
	# First try requests/BeautifulSoup
	try:
		resp = requests.get(url, timeout=10)
		resp.raise_for_status()
		soup = BeautifulSoup(resp.text, "html.parser")
		text = extract_text_from_soup(soup)
		logging.info(f"[Requests] Extracted text ({len(text.split()) if text else 0} words): {text[:200] if text else 'None'}")
		if text and len(text.split()) >= 10:
			return text
	except Exception as e:
		logging.error(f"[Requests] Error: {e}")

	# Fallback uuse Selenium for JS-rendered content
	try:
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--no-sandbox')
		driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
		driver.get(url)
		html = driver.page_source
		driver.quit()
		soup = BeautifulSoup(html, "html.parser")
		text = extract_text_from_soup(soup)
		logging.info(f"[Selenium] Extracted text ({len(text.split()) if text else 0} words): {text[:200] if text else 'None'}")
		if text and len(text.split()) >= 10:
			return text
	except Exception as e:
		logging.error(f"[Selenium] Error: {e}")
	return None
