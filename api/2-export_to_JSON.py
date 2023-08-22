#!/usr/bin/python3
"""task 0"""

import json
import requests
import sys

if __name__ == "__main__":
    users = "https://jsonplaceholder.typicode.com/users/{}"
    todos = "https://jsonplaceholder.typicode.com/todos/?userId={}"

    id = int(sys.argv[1])
    response_users = requests.get(users.format(id)).json()
    response_todos = requests.get(todos.format(id)).json()
    with open('{}.json'.format(id), 'w') as file_csv:
        _list = []
        for id_csv in response_todos:
            if id_csv['userId'] == id:
                _list.append(
                    {"task": id_csv['title'],
                     "completed": id_csv['completed'],
                     "username": response_users['username']})
        json.dump({'{}'.format(id): _list}, file_csv)
