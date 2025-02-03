import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

def search_song(song_name, site):
    query = f"{song_name} site:{site}"
    search_results = list(search(query, num_results=5))
    return search_results[0]  # Get the first search result

def get_audio_link(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # You'd have to customize this part based on the structure of the site.
        # This is an example for detecting audio file links in an <audio> tag.
        audio_tags = soup.find_all('audio', src=True)
        for audio in audio_tags:
            audio_url = audio['src']
            if audio_url.endswith(('.mp3', '.opus')):  # Check if it's an audio file
                return audio_url
    return None

def download_audio(audio_url, filename="downloaded_audio"):
    response = requests.get(audio_url)
    with open(f"{filename}.mp3", "wb") as file:
        file.write(response.content)
    print(f"Audio downloaded as {filename}.mp3")

# Example usage
song_name = "Believer"
site = "xyz.com"  # Replace with actual site name

search_result_url = search_song(input("Song name? "), "https://www.jiosaavn.com/")
if search_result_url:
    print(f"First link found: {search_result_url}")
    audio_url = get_audio_link(search_result_url)
    if audio_url:
        print(f"Audio file found: {audio_url}")
        download_audio(audio_url)
    else:
        print("No audio file found.")
else:
    print("No results found.")
