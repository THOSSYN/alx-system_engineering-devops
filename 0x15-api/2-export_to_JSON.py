#!/usr/bin/python3
"""A script that returns todos of employees bt id"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    userid = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    res = requests.get(f'{url}/todos?userId={userid}')
    res1 = requests.get(f'{url}/users/{userid}')

    res_json = res.json()
    res1_json = res1.json()
    name = res1_json.get('username')
    to_dict = {}
    attr_list = []
    for item in res_json:
        inner_dict = {}
        inner_dict['task'] = item.get('title')
        inner_dict['completed'] = item.get('completed')
        inner_dict['username'] = name
        attr_list.append(inner_dict)
    to_dict[userid] = attr_list

    with open(f'{userid}.json', "w") as f:
        json.dump(to_dict, f)
