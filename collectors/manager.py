from collectors.github import collect as github_collect
from collectors.openai import collect as openai_collect


def collect_all():
    all_data = []

    all_data.extend(github_collect())
    all_data.extend(openai_collect())

    return all_data