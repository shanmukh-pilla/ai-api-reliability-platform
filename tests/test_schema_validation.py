import json

from src.api_client import get_users
from src.schema_validator import validate_schema


def test_user_schema_validation():

    response = get_users()

    user = response.json()[0]

    with open("schemas/user_schema.json") as f:
        schema = json.load(f)

    validate_schema(user, schema)