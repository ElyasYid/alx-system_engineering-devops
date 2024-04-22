#!/usr/bin/python3
"""Export TODO of employee to JSON."""
import json
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(uid)).json()
    uname = u.get("username")
    t = requests.get(url + "todos", params={"userId": uid}).json()

    with open("{}.json".format(uid), "w") as jfile:
        json.dump({uid: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": uname
            } for i in t]}, jfile)
