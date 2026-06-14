import requests
from config import GITHUB_TOKEN

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def github_get(url, params=None):
    """
    Generic GET request to GitHub API.
    """

    response = requests.get(
        url,
        headers=HEADERS,
        params=params
    )

    if response.status_code == 200:
        return response.json()

    print(f"Error {response.status_code}: {response.text}")
    return None