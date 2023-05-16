from dotenv import load_dotenv
import requests
import urllib.parse
import os
from download_image import download_image


def get_file_extension(url):
    path = urllib.parse.urlsplit(url)[2]
    file_extension = os.path.splitext(path)[1]
    return file_extension


def get_apod_images(nasa_api_token):
    url = "https://api.nasa.gov/planetary/apod"
    photo_count = 30
    payload = {
        "api_key": nasa_api_token,
        "count": photo_count
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for image_number, image in enumerate(response.json(), start=1):
        link = image["url"]
        file_extension = get_file_extension(link)
        if not file_extension:
            continue
        filename = f"images/apod_{image_number}{file_extension}"
        download_image(link, filename)


def main():
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_TOKEN")
    get_apod_images(nasa_api_token)


if __name__ == "__main__":
    main()
