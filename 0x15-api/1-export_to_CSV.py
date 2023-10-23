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

    res1_json = res1.json()
    name = res1_json.get('username')

    to_json = res.json()

    with open(f'{userid}.csv', "w", newline='') as fptr:
        content = csv.writer(fptr, quoting=csv.QUOTE_ALL)
        for item in to_json:
            content.writerow([
                item["userId"],
                f'{name}',
                item["completed"],
                item["title"]
            ])
