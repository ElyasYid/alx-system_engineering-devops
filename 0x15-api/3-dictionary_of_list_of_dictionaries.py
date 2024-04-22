#!/usr/bin/python3
"""Exports TODO of all employees to JSON."""
import json
import requests

if __name__ == "__main__":
    u = "https://jsonplaceholder.typicode.com/"
    us = requests.get(u + "users").json()

    with open("todo_all_employees.json", "w") as jf:
        json.dump({
            i.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": i.get("username")
            } for t in requests.get(u + "todos",
                                    params={"userId": i.get("id")}).json()]
            for i in us}, jf)
