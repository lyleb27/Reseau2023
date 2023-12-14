import aiohttp
import aiofiles
import asyncio

async def get_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error fetching content from {url}: {e}")
        return None

async def write_content(content, file):
    try:
        async with aiofiles.open(file, 'w', encoding='utf-8') as f:
            await f.write(content)
        print(f"Content written to {file}")
    except IOError as e:
        print(f"Error writing content to {file}: {e}")

async def main(url):
    content = await get_content(url)

    if content:
        await write_content(content, '/tmp/web_page')
    else:
        print("Failed to fetch content.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python web_async.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    asyncio.run(main(url))
