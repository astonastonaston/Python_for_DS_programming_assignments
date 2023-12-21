import random

# When is an empty dictionary a valid output?
# Functional Points = 14/14
# Validation Points = 0/6
# Based upon common mistakes, but maybe not your specific mistake, it could be that..
# When is an empty dictionary a valid output?


def map_bitstring(x):
    """
    Input: Height and width of a rectangle\n
    Return: Area of the rectangle
    """
    assert type(x)==list
    mapbit = {}
    for i in list(set(x)):
        if (i.count("0") > i.count("1")):
            mapbit[i] = 0 
        else:
            mapbit[i] = 1
    return mapbit 
            







def main():
    x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
    print(map_bitstring(x))
    # print(get_sample())
    return 0

main()