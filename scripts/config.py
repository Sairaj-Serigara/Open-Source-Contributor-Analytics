import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# GitHub Personal Access Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# GitHub API Base URL
BASE_URL = "https://api.github.com"

# Repositories to analyze
REPOSITORIES = [
    ("facebook", "react"),
    ("microsoft", "vscode"),
    ("tensorflow", "tensorflow")
]