#!/usr/bin/python3
""" A script that defines a function """


def recurse(subreddit, hot_list=[]):
    """ A function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit. If no results are found for
    the given subreddit, the function should return None.
    Requirements:
     - You may change the prototype, but it must be able to be called with just
       a subreddit supplied. AKA you can add a counter, but it must work without
       supplying a starting value in the main.
     - If not a valid subreddit, return None.
     NOTE: Invalid subreddits may return a redirect to search results.
           Ensure that you are not following redirects.
    """
    import requests

    hdrs = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }
    limit = 10
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    try:
        response = requests.get(url, headers=hdrs,
                                allow_redirects=False)
        if response.status_code == 200:
            resdata = response.json()
            if resdata.get("data") and resdata["data"].get("children"):
                posts = resdata["data"]["children"][:limit]
                if posts:
                    for post in posts:
                        print(post["data"]["title"] or None)
                else:
                    print(None)
            else:
                print(None)
        else:
            print(None)
    except Exception:
        print(None)
