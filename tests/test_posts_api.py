from src.api_client import get_posts


def test_posts_api():

    response = get_posts()

    assert response.status_code == 200

    posts = response.json()

    assert len(posts) > 0