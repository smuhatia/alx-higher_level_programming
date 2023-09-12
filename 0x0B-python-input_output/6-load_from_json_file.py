#!/usr/bin/python3
"""Create object from a JSON file
json.load(f) is used to deserialize f (which in this
case is our file) to a Python object."""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
