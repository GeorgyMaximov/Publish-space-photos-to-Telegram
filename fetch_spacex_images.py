import requests
import argparse
from download_image import download_image
import os


def fetch_spacex_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    links = response.json()["links"]["flickr"]["original"]
    for link_number, link in enumerate(links):
        filename = f"images/spacex_{link_number}.jpg"
        download_image(url, filename)


def main():
    os.makedirs("images", exist_ok=True)
    parser = argparse.ArgumentParser(description="Get photos from SpaceX launch.")
    parser.add_argument("-l", "--launch_id", default="latest", help="Get photos from the specified launch.")
    args = parser.parse_args()
    fetch_spacex_launch(args.launch_id)


if __name__ == "__main__":
    main()
