import random

# When is an empty dictionary a valid output?
# Functional Points = 14/14
# Validation Points = 0/6
# Based upon common mistakes, but maybe not your specific mistake, it could be that..
# When is an empty dictionary a valid output?


def get_sample(nbits=3,prob=None,n=1):
    """
    Input: Height and width of a rectangle\n
    Return: Area of the rectangle
    """
    assert (type(nbits)==int)
    assert (nbits>0)
    assert (type(n)==int)
    assert (n>0)
    assert (type(prob)==dict)
    assert (prob!=None)
    # if ((nbits==0) or (n==0) or (prob==None)):
    #     return []
    assert (len(prob) == 2**nbits)
    for i in list(prob.keys()):
        assert type(i)==str
        assert len(i)==nbits
        assert all(c in '01' for c in i)
    assert (sum(list(prob.values())) == 1)

    return random.choices(list(prob.keys()), k=n, weights= list(prob.values()))


# def main():
#     p={'000': 0.125, 
#     '001': 0.125, 
#     '010': 0.125, 
#     '011': 0.125, 
#     '100': 0.125, 
#     '101': 0.125, 
#     '110': 0, 
#     '111': 0.25} 
#     print(get_sample(nbits=3,prob=p,n=5))
#     # print(get_sample())
#     return 0

# main()