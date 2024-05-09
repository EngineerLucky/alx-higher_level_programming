#!/usr/bin/python3
""" The Algorithms for a list of integers."""


def find_peak(list_of_integers):
    """ The function finds a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]i
