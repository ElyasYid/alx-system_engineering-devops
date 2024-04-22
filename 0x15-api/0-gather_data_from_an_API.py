#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    u = "https://jsonplaceholder.typicode.com/"
    e = requests.get(u + "users/{}".format(sys.argv[1])).json()
    t = requests.get(u + "todos", params={"userId": sys.argv[1]}).json()

    c = [i.get("title") for i in t if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        e.get("name"), len(c), len(t)))
    [print("\t {}".format(i)) for i in c]
