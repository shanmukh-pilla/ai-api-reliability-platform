import requests

from src.config import BASE_URL


def get_users():
    return requests.get(f"{BASE_URL}/users")


def get_posts():
    return requests.get(f"{BASE_URL}/posts")