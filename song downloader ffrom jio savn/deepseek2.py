import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re
import time

def find_media_url(page_content, base_url):
    # Try different patterns for finding audio files
    patterns = [
        r'"media_url":"(https://[^"]+\.mp3)"',
        r'src="(https://[^"]+\.mp3)"',
        r'data-url="(https://[^"]+\.mp3)"',
        r'"preview_url":"(https://[^"]+\.mp3)"'
    ]

    for pattern in patterns:
        match = re.search(pattern, page_content)
        if match:
            return match.group(1).replace('\\', '')

    # Try HTML5 audio tags
    soup = BeautifulSoup(page_content, 'html.parser')
    audio_tag = soup.find('audio')
    if audio_tag and audio_tag.get('src'):
        return requests.compat.urljoin(base_url, audio_tag['src'])

    return None

def download_song():
    song_name = input("Enter song name: ").strip()
    query = f'{song_name} site:jiosaavn.com'

    try:
        # Get first Google result with custom headers
        print("Searching Google...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }

        # Handle possible search errors
        try:
            search_results = search(query, num=3, stop=3, pause=5, user_agent=headers['User-Agent'])
            first_url = next(search_results)
        except StopIteration:
            print("No search results found")
            return
        except Exception as e:
            print(f"Google search failed: {str(e)}")
            return

        print(f"Trying URL: {first_url}")

        # Fetch page with retries
        for _ in range(3):
            try:
                response = requests.get(first_url, headers=headers)
                response.raise_for_status()
                break
            except requests.exceptions.RequestException:
                time.sleep(2)
        else:
            print("Failed to fetch page after 3 attempts")
            return

        # Find media URL
        media_url = find_media_url(response.text, first_url)
        if not media_url:
            print("Failed to find audio URL in page content")
            return

        print(f"Found media URL: {media_url}")

        # Download with stream and progress
        print("Starting download...")
        response = requests.get(media_url, headers=headers, stream=True)
        response.raise_for_status()

        filename = f"{song_name.replace(' ', '_')}.mp3"
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)

        print(f"Successfully downloaded: {filename}")

    except Exception as e:
        print(f"Final error: {str(e)}")

if __name__ == "__main__":
    download_song()