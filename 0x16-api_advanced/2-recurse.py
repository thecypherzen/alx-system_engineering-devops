#!/usr/bin/python3
""" A script that defines a function """


def recurse(subreddit, hot_list=[])
    """ A recursive function that queries the Reddit API and returns a
        list containing the titles of all hot articles for a given
        subreddit. If no results are found for the given subreddit, the
        function should return None.

        Hint: The Reddit API uses pagination for separating pages of
              responses.

        Requirements:
        - If not a valid subreddit, return None.
        - NOTES:
          - Invalid subreddits may return a redirect to search results.
            Ensure that you are not following redirects.
          - You may change the prototype, but it must be able to be
            called with just a subreddit supplied. AKA you can add a
            counter, but it must work without supplying a starting value
            in the main.
    """
    import requests
    import json

    hdrs = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }
    limit = 10
    url = f"https://www.reddit.com/r/{subreddit}/hot.json" + \
        f"?limit={limit}&raw_json=1"
    print(url)
    response = requests.get(url, headers=hdrs,
                            allow_redirects=False)
    if response.status_code == 200:
        objs = response.json()["data"]["children"]
        while len(objs) > limit:
            objs.pop()
        for obj in objs:
            print(obj["data"]["title"])
    else:
        return print("None")
