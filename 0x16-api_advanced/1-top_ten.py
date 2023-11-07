#!/usr/bin/python3
"""A script that returns first 10 post of a subreddit"""

import requests


def top_ten(subreddit):
    """Finds the first ten post of a subreddit
       Args:
         sunbreddit (str): A reddit endpoint

       Return:
         None if subreddit is invalid
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(
                url,
                headers={'User-agent': 'Chrome/58.0.3029.110  Safari/537.36'}
                )

    if response.status_code == 200:
        response_to_json = response.json()
        post_list = response_to_json['data']['children']
        for post in post_list[:10]:
            post_title = post['data']['title']
            print(post_title)
    else:
        print(None)
