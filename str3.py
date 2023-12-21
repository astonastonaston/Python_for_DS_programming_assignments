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
            
def gather_values(x):
    """
    Input: Height and width of a rectangle\n
    Return: Area of the rectangle
    """
    assert type(x)==list
    gatval = {}
    for i in x:
        if (i.count("0") > i.count("1")):
            if (i not in list(gatval.keys())):
                gatval[i] = [0]
            else:
                gatval[i].append(0)
        else:
            if (i not in list(gatval.keys())):
                gatval[i] = [1]
            else:
                gatval[i].append(1)
    return gatval 
    
def threshold_values(seq,threshold=1):
    """
    Input: Height and width of a rectangle\n
    Return: Area of the rectangle
    """
    assert type(seq)==list
    gatseq = gather_values(seq)
    assert len(gatseq)>=threshold
    gatseqSel = sorted(gatseq.items(), key=lambda item: (-item[1].count(1), int(item[0], 2)))[:threshold] 
    gatseqSel = [i[0] for i in gatseqSel]
    
    for i in list(gatseq.keys()):
        if i in gatseqSel:
            gatseq[i] = 1
        else:
            gatseq[i] = 0

    return gatseq






# def main():
#     seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
#     print(threshold_values(seq,3))
#     # print(get_sample())
#     return 0

# main()