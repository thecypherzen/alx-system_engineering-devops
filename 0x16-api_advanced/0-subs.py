#!/usr/bin/python3
""" A script that defines a function """


def number_of_subscribers(subreddit):
    """ A function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit. If an invalid subreddit is given, the function should
        return 0.

        NOTE: No authentication is necessary for most features of the Reddit
              API. If you’re getting errors related to Too Many Requests,
              ensure you’re setting a custom User-Agent.

        Requirements:
        - If not a valid subreddit, return 0.
        - NOTE: Invalid subreddits may return a redirect to search results.
                Ensure that you are not following redirects.
    """
    import requests


    hdrs = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=hdrs,
                            allow_redirects=False)
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    return 0
