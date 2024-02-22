#!/usr/bin/python3
"""The function add_attribute contains function that checks.
"""


def add_attribute(obj, name, value):
    """The function adds a new attribute to an object if it’s possible."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
