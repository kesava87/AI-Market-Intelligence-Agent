import requests
from models.data_model import create_item
def collect():
    url = "https://api.github.com/search/repositories"

    params = {
        "q": "artificial intelligence",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("GitHub API Error")
        return []

    data = response.json()

    repositories = data["items"]

    results = []

    for repo in repositories:
        results.append(
    create_item(
        title=repo["full_name"],
        description=repo["description"],
        link=repo["html_url"],
        source="GitHub",
        stars=repo["stargazers_count"],
        language=repo["language"]
    )
)
        

    return results