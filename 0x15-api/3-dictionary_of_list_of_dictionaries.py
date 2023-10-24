#!/usr/bin/python3
"""A script that returns todos of employees bt id"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    res = requests.get(f'{url}/todos')
    user_res = requests.get(f'{url}/users')

    json_details = res.json()
    users_json = user_res.json()

    user_dict = {user['id']: user['username'] for user in users_json}

    to_dict = {}
    for todo in json_details:
        inner_dict = {}
        user_id = todo['userId']
        username = user_dict.get(user_id)
        task = todo.get('title')
        completed = todo.get('title')

        if user_id not in to_dict:
            to_dict[user_id] = []

        to_dict[user_id].append({
            'username': username,
            'task': task,
            'complete': completed
            })

    with open('todo_all_employees.json', "w") as fptr:
        json.dump(to_dict, fptr)
