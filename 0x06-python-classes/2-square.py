#!/usr/bin/python3

"""It Defines a class Square."""


class Square:
    """It Represent a square."""

    def __init__(self, size=0):
        """It must Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
