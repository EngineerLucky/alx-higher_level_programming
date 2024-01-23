#!/usr/bin/python3

def magic_calculation(a, b):
    """bytecode provided."""
    from magic_calculation_102 import add, sub

    if a < b:
        p = add(a, b)
        for i in range(4, 6):
            p = add(p, i)
        return (p)

    else:
        return(sub(a, b))
