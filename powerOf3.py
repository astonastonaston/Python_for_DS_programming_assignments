import itertools

def get_power_of3(num):
    """
    Input: Height and width of a rectangle\n
    Return: Area of the rectangle
    """
    assert (type(num)==int)
    assert ((num<=40) & (num>=0))
    ws = itertools.product([-1, 0, 1], repeat=4)
    ns = [1, 3, 9, 27]
    for w in ws:
        sum = w[0]*ns[0] + w[1]*ns[1] + w[2]*ns[2] + w[3]*ns[3]
        if (sum == num):
            return list(w)
    return [0,0,0,0]


def main():
    print(get_power_of3(10))
    return 0

main()