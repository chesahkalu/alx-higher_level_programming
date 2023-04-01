#!/usr/bin/python3
"""list 10 most recent of a repository,
- You must use the GitHub API, 
- the documentation https://developer.github.com/v3/repos/commits/
- Print all commits by: `<sha>: <author name>` (one by line)
Eg: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
