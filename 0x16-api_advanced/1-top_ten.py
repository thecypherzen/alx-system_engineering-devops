#!/usr/bin/python3
""" A script that defines a function """


def top_ten(subreddit):
    """ A function that queries the Reddit API and and prints the titles
        of the first 10 hot posts listed for a given subreddit.

        Requirements:
        - If not a valid subreddit, print None.
        - NOTE: Invalid subreddits may return a redirect to search results.
                Ensure that you are not following redirects.
    """
    import requests
    import json

    hdrs = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }
    limit = 10
    url = f"https://www.reddit.com/r/{subreddit}.json" + \
        f"?sort=top&limit={limit}"
    print(url)
    response = requests.get(url, headers=hdrs,
                            allow_redirects=False)
    if response.status_code == 200:
        objs = response.json()["data"]["children"][0:limit]
        for obj in objs:
            print(obj["data"]["title"])
    else:
        return print(None)
