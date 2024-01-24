#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    averag = 0
    divid = 0
    for tup in my_list:
        averag += tup[0] * tup[1]
        divid += tup[1]
    return float(averag / divid)
