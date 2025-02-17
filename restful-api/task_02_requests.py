#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""

import requests
import csv


def fetch_and_print_posts():
    """
    fetch_and_print_posts function
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    fetch_and_save_posts function
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'],
                                    extrasaction="ignore")
            writer.writeheader()
            posts = response.json()
            writer.writerows(posts)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
