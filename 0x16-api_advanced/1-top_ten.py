#!/usr/bin/python3
"""gets info from reddit api"""


def top_ten(subreddit):
    """function returns the top 10 hot posts
    of the subreddit"""
    import requests

    subs = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subs.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in subs.json().get("data").get("children")]
