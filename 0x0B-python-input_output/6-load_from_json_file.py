#!/usr/bin/python3
"""The function save_to_json_file contains

a function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”."""
    with open(filename, 'r') as f:
        return json.load(f)
