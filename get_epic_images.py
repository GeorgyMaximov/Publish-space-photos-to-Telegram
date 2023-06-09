import requests
import datetime
import os
from dotenv import load_dotenv
from download_image import download_image


def get_epic_images(nasa_api_token):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": nasa_api_token
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number_image, features_image in enumerate(response.json()):
        date_image = features_image["date"]
        date = datetime.datetime.fromisoformat(date_image).date().strftime("%Y/%m/%d")
        name_image = features_image["image"]
        link = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name_image}.png"
        filename = f"images/epic_{number_image}.png"
        download_image(link, filename, payload)


def main():
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_TOKEN")
    get_epic_images(nasa_api_token)


if __name__ == "__main__":
    main()
