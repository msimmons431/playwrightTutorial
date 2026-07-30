import random

import pytest


class TestSetup:
    @classmethod
    def setup_class(cls):
        print("Setting up class")
        cls.numlist = [random.randint(1, 33) for i in range(0, 10)]

    @classmethod
    def teardown_class(cls):
        print("Tearing down class")
        cls.numlist.clear()

    def test_one(self):
        print(f"Test one The list: {self.numlist}")
        assert len(self.numlist) > 5

    def test_two(self):
        print(f"Test two The list: {self.numlist}")
        assert len(self.numlist) > 5

    def test_three(self):
        print(f"Test three The list: {self.numlist}")
        assert len(self.numlist) > 5


def test_four(return_a_random_string):
    print(f"Test four ( fixture from conftest ) The string: {return_a_random_string}")


# def test_five(return_some_json_data):
# print(f"Test five ( fixture from conftest ) The dict {return_some_json_data}.")
# for k,v in return_some_json_data.items():
# if k == "likes":
# print(f"Printing v type: {type(v)}")
# snakes = { k: v for k,v in return_some_json_data.items() if k == "likes" if  "snakes" in v }
# print(f"Printing snakes: {snakes}")


def test_six():
    foo = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print("Test six just build a list via list comprehension")
    # I want to randomly select 3 values from foo
    x = [foo[random.randint(0, 9)] for i in range(0, 3)]
    print(f"Test six 3 random values from foo: {x}")
