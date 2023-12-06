import os
import sys
import aiohttp
import asyncio
import time

async def get_content(url, session):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def write_content(content, file):
    try:
        directory = os.path.dirname(file)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Content written to {file}")
    except IOError as e:
        print(f"Error writing content to {file}: {e}")

async def process_url(url, session):
    content = await get_content(url, session)
    if content:
        file_name = f"/tmp/web_{url.replace('https://', '').replace('http://', '').replace('/', '_')}"
        write_content(content, file_name)
    else:
        print(f"Failed to fetch content from {url}")

async def process_urls(file_path):
    try:
        async with aiohttp.ClientSession() as session:
            with open(file_path, 'r') as file:
                urls = file.readlines()
                tasks = [process_url(url.strip(), session) for url in urls]
                await asyncio.gather(*tasks)
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python web_async_multiple.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]

    start_time = time.time()

    asyncio.run(process_urls(file_path))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Total execution time: {elapsed_time:.2f} seconds")
