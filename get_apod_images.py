from unittest import skip
from dotenv import load_dotenv
import requests
import urllib.parse
import os
from download_image import download_image


def get_file_extension(url):
    path = urllib.parse.urlsplit(url)[2]
    file_extension = os.path.splitext(path)[1]
    return file_extension


def get_apod_images(nasa_api):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": nasa_api,
        "count": 30
    }
    response = requests.get(url, params=payload)
    for image_number, image in enumerate(response.json(), start=1):
        link = image["url"]
        file_extension = get_file_extension(link)
        if file_extension == "":
            continue
        filename = f"images/apod_{image_number}{file_extension}"
        download_image(link, filename)


def main():
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_api = os.getenv("NASA_API")
    get_apod_images(nasa_api)


if __name__ == "__main__":
    main()