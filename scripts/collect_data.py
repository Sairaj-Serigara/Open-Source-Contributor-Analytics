from config import BASE_URL, REPOSITORIES
from github_api import github_get

owner, repo = REPOSITORIES[0]

url = f"{BASE_URL}/repos/{owner}/{repo}"

data = github_get(url)

if data:
    print("Repository:", data["full_name"])
    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])