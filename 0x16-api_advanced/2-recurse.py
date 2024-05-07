#!/usr/bin/python3
"""gets info from reddit api"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """function returns all hot posts
    of the subreddit"""
    import requests

    subs = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        params={"count": count, "after": after},
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subs.status_code >= 400:
        return None

    hotty = hot_list + [child.get("data").get("title")
                        for child in subs.json()
                        .get("data")
                        .get("children")]

    subfo = subs.json()
    if not subfo.get("data").get("after"):
        return hotty

    return recurse(subreddit, hotty, subfo.get("data").get("count"),
                   subfo.get("data").get("after"))
