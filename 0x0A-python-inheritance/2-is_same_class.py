#!/usr/bin/python3
"""The function 

that contains function that compares an object with an instance.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    """
    return type(obj) is a_class
