import json
import random
import string

import pytest


@pytest.fixture
def return_a_random_string():
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


@pytest.fixture
def return_some_json_data() -> dict:
    with open("files/readfile", "r") as f:
        data = json.load(f)
    return data[0]
