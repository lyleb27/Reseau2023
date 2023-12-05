import os
import requests

def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def write_content(content, file):
    try:
        # Create the directory if it doesn't exist
        directory = os.path.dirname(file)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Content written to {file}")
    except IOError as e:
        print(f"Error writing content to {file}: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    content = get_content(url)

    if content:
        write_content(content, '/tmp/web_page')
    else:
        print("Failed to fetch content.")
