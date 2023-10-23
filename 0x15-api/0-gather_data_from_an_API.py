#!/usr/bin/python3
"""A script that returns todos of employees bt id"""

import json
import sys
import urllib.request


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    userId = sys.argv[1]

    req = urllib.request.Request(f"{url}/users/{userId}")
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        to_json = json.loads(html)

    with urllib.request.urlopen(f"{url}/todos?userId={userId}") as response:
        html2 = response.read().decode('utf-8')
        todo_json = json.loads(html2)

        count = 0
        check_list = ""
        for todo in todo_json:
            task_done = todo['completed']
            if task_done is True:
                count = count + 1
                check_list += "\t" + todo['title'] + "\n"

    name = to_json['name']
    total = len(todo_json)
    print(
        "Employee {} is done with tasks({}/{}):"
        .format(name, count, total))
    print(check_list)
