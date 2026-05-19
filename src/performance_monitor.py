import time


def measure_response_time(api_function):

    start = time.time()

    response = api_function()

    end = time.time()

    return response, end - start