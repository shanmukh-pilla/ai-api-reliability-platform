from src.api_client import get_users


def test_users_api():

    response = get_users()

    assert response.status_code == 200

    users = response.json()

    assert len(users) > 0