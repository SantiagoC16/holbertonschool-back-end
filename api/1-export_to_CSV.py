#!/usr/bin/python3
"""task 0"""

import requests
import sys

if __name__ == "__main__":
    users = "https://jsonplaceholder.typicode.com/users/{}"
    todos = "https://jsonplaceholder.typicode.com/todos/?userId={}"

    id = int(sys.argv[1])
    response_users = requests.get(users.format(id)).json()
    response_todos = requests.get(todos.format(id)).json()
    with open('{}.csv'.format(id), 'w') as file_csv:
        for id_csv in response_todos:
            if id_csv['userId'] == id:
                file_csv.write('"{}", "{}", "{}", "{}"\n'.format(
                    id, response_users['username'],
                    id_csv['completed'], id_csv['title']))
