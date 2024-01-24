#!/usr/bin/python3
def search_replace(my_list, search, replace):
    take = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            take.append(replace)
        else:
            take.append(my_list[i])
    return take
