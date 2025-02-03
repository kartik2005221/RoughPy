import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def find_media_url(page_source):
    # Try to find encoded media URLs commonly used by JioSaavn
    patterns = [
        r'"mediaUrl":"(https:\\/\\/[^"]+\.mp3)"',
        r'"encrypted_media_url":"(https:\\/\\/[^"]+\.mp3)"',
        r'"perma_url":"(https:\\/\\/[^"]+)"',
        r'"media_preview_url":"(https:\\/\\/[^"]+\.mp3)"'
    ]

    for pattern in patterns:
        match = re.search(pattern, page_source)
        if match:
            url = match.group(1).replace('\\/', '/')
            return url.replace('_96_p.mp3', '_320.mp3')
    return None

def download_song():
    song_name = input("Enter song name: ").strip()

    # Setup Chrome with Selenium
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # Step 1: Google search
        print("Searching Google...")
        search_url = f"https://www.google.com/search?q={song_name}+site%3Ajiosaavn.com"
        driver.get(search_url)

        # Accept cookies if needed
        try:
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Accept')]"))
            ).click()
        except:
            pass

        # Get first search result
        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='search']//a"))
        )
        jio_url = first_result.get_attribute("href")
        print(f"Found JioSaavn URL: {jio_url}")

        # Step 2: Visit JioSaavn page
        print("Visiting JioSaavn...")
        driver.get(jio_url)
        time.sleep(3)  # Wait for JavaScript to load

        # Find media URL in page source
        page_source = driver.page_source
        media_url = find_media_url(page_source)

        if not media_url:
            print("Failed to find media URL in page source")
            return

        print(f"Found media URL: {media_url}")

        # Step 3: Download the file
        print("Starting download...")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Referer": jio_url
        }

        response = requests.get(media_url, headers=headers, stream=True)
        response.raise_for_status()

        filename = f"{song_name.replace(' ', '_')}.mp3"
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Successfully downloaded: {filename}")

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    download_song()