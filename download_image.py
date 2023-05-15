import requests


def download_image(url, filename, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)