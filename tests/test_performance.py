from src.performance_monitor import measure_response_time
from src.api_client import get_users
from src.config import MAX_RESPONSE_TIME


def test_users_api_performance():

    response, response_time = measure_response_time(get_users)

    assert response.status_code == 200

    assert response_time < MAX_RESPONSE_TIME