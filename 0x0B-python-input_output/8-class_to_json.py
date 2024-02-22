#!/usr/bin/python3
"""The function class_to_json module Contains a function that returns a dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    structure."""
    return obj.__dict__
