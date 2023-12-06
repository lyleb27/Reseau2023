import os
import sys
import requests
import time

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

def process_urls(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                if not url.startswith('http'):
                    url = 'http://' + url

                file_name = f"/tmp/web_{url.replace('https://', '').replace('http://', '').replace('/', '_')}"
                content = get_content(url)

                if content:
                    write_content(content, file_name)
                else:
                    print(f"Failed to fetch content from {url}")
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python web_sync_multiple.py <file_path>")
        sys.exit(1)
file_path = sys.argv[1]

start_time = time.time()  # Enregistre le temps de début

process_urls(file_path)

end_time = time.time()  # Enregistre le temps de fin
elapsed_time = end_time - start_time

print(f"Total execution time: {elapsed_time:.2f} seconds")
