import sys
from src.api import analyze_blog

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_blog.py <blog_url>")
        sys.exit(1)
    url = sys.argv[1]
    result = analyze_blog(url)
    print(result)
