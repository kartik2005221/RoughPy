import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

def find_media_url(page_content, base_url):
    # Try to find audio tags
    soup = BeautifulSoup(page_content, 'html.parser')
    audio_tags = soup.find_all('audio')
    for audio in audio_tags:
        if audio.get('src'):
            return requests.compat.urljoin(base_url, audio['src'])

    # Search for common audio patterns in scripts
    script_pattern = re.compile(r'"(https?://[^"]+\.(?:mp3|opus))"')
    matches = script_pattern.findall(page_content)
    if matches:
        return matches[0]

    # Look for JSON data with media information
    json_pattern = re.compile(r'\{.*"media_url":\s*"([^"]+)".*\}', re.DOTALL)
    json_match = json_pattern.search(page_content)
    if json_match:
        return json_match.group(1)

    return None

def download_song():
    song_name = input("Enter song name: ").strip()
    query = f'"{song_name}" site:https://www.jiosaavn.com/'

    try:
        # Get first Google result
        search_results = search(query, num=1, stop=1, pause=2, user_agent='Mozilla/5.0')
        first_url = next(search_results)
        print(f"Found URL: {first_url}")

        # Fetch the page content
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(first_url, headers=headers)
        response.raise_for_status()

        # Find media URL
        media_url = find_media_url(response.text, first_url)
        if not media_url:
            print("No media URL found")
            return

        # Download the file
        print(f"Attempting to download from: {media_url}")
        media_response = requests.get(media_url, headers=headers, stream=True)
        media_response.raise_for_status()

        filename = f"{song_name.replace(' ', '_')}.mp3"
        with open(filename, 'wb') as f:
            for chunk in media_response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Successfully downloaded: {filename}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    download_song()