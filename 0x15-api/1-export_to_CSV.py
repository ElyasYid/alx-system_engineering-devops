#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(uid)).json()
    uname = u.get("username")
    t = requests.get(url + "todos", params={"userId": uid}).json()

    with open("{}.csv".format(uid), "w", newline="") as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [w.writerow(
            [uid, uname, i.get("completed"), i.get("title")]
         ) for i in t]
