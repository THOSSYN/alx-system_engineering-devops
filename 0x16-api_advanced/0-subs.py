#!/usr/bin/python3
"""A script that queries Reddit api for subreddit subcribers"""

import requests


def number_of_subscribers(subreddit):
    """Request Reddit api and returns nos of subscribers
       Args:
         Arg1 (str): the subreddit endpoint
       Return:
         0 if subreddit is invalid or list of subscribers
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(
                url,
                headers={'User-Agent': 'Chrome/58.0.3029.110 Safari/537.36'}
                )

    if response.status_code == 200:
        subreddit_data = response.json()
        subscribers_count = subreddit_data['data']['subscribers']
        return subscribers_count
    else:
        return 0
