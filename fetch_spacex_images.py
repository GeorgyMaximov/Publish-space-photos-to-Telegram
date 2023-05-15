import requests
import argparse
from download_image import download_image
import os


def fetch_spacex_launch(args):
    if args.launch_id:
        url = f"https://api.spacexdata.com/v5/launches/{args.launch_id}"
    else:
        url = "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(url)
    links = response.json()["links"]["flickr"]["original"]
    for link_number, link in enumerate(links):
        filename = f"images/spacex_{link_number}.jpg"
        download_image(url, filename)


def main():
    os.makedirs("images", exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--launch_id")
    args = parser.parse_args()
    fetch_spacex_launch(args)


if __name__ == "__main__":
    main()