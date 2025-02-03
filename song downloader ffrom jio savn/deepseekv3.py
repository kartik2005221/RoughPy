import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re
import time

def find_media_url(page_content, base_url):
    # Updated patterns for JioSaavn's current structure
    patterns = [
        r'"mediaUrl":"(https://[^"]+\.mp3)"',
        r'"encrypted_media_url":"(https://[^"]+\.mp3)"',
        r'src="(https://[^"]+\.mp3)"',
        r'data-src="(https://[^"]+\.mp3)"'
    ]

    for pattern in patterns:
        match = re.search(pattern, page_content)
        if match:
            url = match.group(1).replace('\\', '')
            return url.replace('_96.mp3', '_320.mp3')  # Try higher quality

    return None

def download_song():
    song_name = input("Enter song name: ").strip()
    query = f'{song_name} site:jiosaavn.com'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }

        print("Searching Google...")
        try:
            # Fixed search parameters for new library version
            search_results = search(
                query,
                num_results=3,
                sleep_interval=5,
                user_agent=headers['User-Agent']
            )
            first_url = next(iter(search_results))
        except Exception as e:
            print(f"Google search failed: {str(e)}")
            return

        print(f"Trying URL: {first_url}")

        # Added referer header and timeout
        response = requests.get(first_url, headers=headers, timeout=10)
        response.raise_for_status()

        # Handle URL encoding
        media_url = find_media_url(response.text, first_url)
        if not media_url:
            print("Failed to find audio URL in page content")
            return

        print(f"Found media URL: {media_url}")

        # Modified download headers
        download_headers = headers.copy()
        download_headers.update({
            'Referer': first_url,
            'Accept': '*/*',
            'Sec-Fetch-Mode': 'no-cors'
        })

        response = requests.get(media_url, headers=download_headers, stream=True)
        response.raise_for_status()

        filename = f"{song_name.replace(' ', '_')}.mp3"
        with open(filename, 'wb') as f:
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    print(f"Downloaded {downloaded}/{total_size} bytes", end='\r')

        print(f"\nSuccessfully downloaded: {filename}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    download_song()