#!/usr/bin/python3
"""task 3"""

import json
import requests

if __name__ == "__main__":
    users = "https://jsonplaceholder.typicode.com/users/"
    todos = "https://jsonplaceholder.typicode.com/todos/"

    response_users = requests.get(users).json()
    response_todos = requests.get(todos).json()
    with open('todo_all_employees.json', 'w') as file_json:
        _list = []
        _dict = {}
        for _id in response_users:
            id = _id['id']
            for tasks in response_todos:
                if tasks['userId'] == id:
                    _list.append(
                        {"task": tasks['title'],
                         "completed": tasks['completed'],
                         "username": _id['username']})
            _dict[id] = _list
            _list = []
        json.dump(_dict, file_json)
