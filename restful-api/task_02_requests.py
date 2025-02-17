#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""

import requests
import json
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
        posts_data = []
        posts = response.json()
        for post in posts:
            post_info = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            posts_data.append(post_info)
    with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts_data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
