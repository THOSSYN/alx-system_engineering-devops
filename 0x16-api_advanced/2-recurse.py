#!/usr/bin/python3
"""A script that recursively quries a Reddit api
   and returns a list of all articles title
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Uses recuresion to request an api
       Args:
         subreddit (str): A reddit endpoint
         hot_list (list): A list of article titles

       Return:
         None if subreddit is invalid or a list of titles
    """
    params = {'limit': 25}

    if after:
        params['after'] = after

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(
                    url,
                    params=params,
                    headers={
                        'User-agent': 'Chrome/58.0.3029.110  Safari/537.36'
                        }
                    )

    if response.status_code != 200:
        return None

    response_to_json = response.json()
    post_list = response_to_json['data']['children']

    for post in post_list:
        title = post['data']['title']
        hot_list.append(title)

    after = response_to_json['data']['after']

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
