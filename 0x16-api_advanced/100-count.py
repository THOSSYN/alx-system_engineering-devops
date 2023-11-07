#!/usr/bin/python3
"""A script that counts the number of occurence
   of keyword from a response from a subreddit
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """Counts occurrences of each word in word_list in the given subreddit.

    Args:
        subreddit (str): The Reddit endpoint.
        word_list (list): Words to count occurrences of.

    Returns:
        None: If the subreddit is invalid or no results are found.
    """
    if count_dict is None:
        count_dict = {}

    params = {'limit': 25}

    if after:
        params['after'] = after

    url = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&show=all&t=all'

    response = requests.get(
        url,
        headers={'User-agent': 'Chrome/58.0.3029.110 Safari/537.36'},
        params=params)

    if response.status_code != 200:
        return None

    response_to_json = response.json()
    post_list = response_to_json.get('data', {}).get('children', [])

    for post in post_list:
        title = post['data']['title'].upper()
        for word in word_list:
            if word.upper() in title:
                count_dict[word] = count_dict.get(word, 0) + 1

    after = response_to_json['data']['after']

    if after:
        count_words(subreddit, word_list, after, count_dict)
    else:
        print_results(count_dict)


def print_results(word_list):
    """Helper function for printing count and word"""
    word_counts = {}
    for word, count in zip(word_list, range(len(word_list))):
        word_counts[word.lower()] = count
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
