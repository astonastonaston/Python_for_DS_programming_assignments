def get_trapped_water(seq):
    """Compute the amount of water trapped, given the wall height sequence"""
    n = len(seq)
    water = 0
    for i in range(1, n-1):
        if (i == 1):
            left, right = max(seq[:i]), max(seq[i+1:])
        else:
            left = max(left, seq[i-1])
            if (seq[i]==right):
                right = max(seq[i+1:])
        water += max(0, min(left, right) - seq[i]) 
    return water


# def main():
#     seq = [3, 0, 1, 3, 0, 5]
#     print(get_trapped_water(seq))
#     return 0

# main()