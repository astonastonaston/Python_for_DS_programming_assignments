
def slide_window(x,width,increment):
    """
    Input: Height and width of a rectangle\n
    Return: Area of the rectangle
    """
    assert (type(x)==list)
    assert ((width>0) & (increment>0))
    res = []
    ind = 0
    while (ind + width <= len(x)):
        res.append(x[ind:ind+width])
        ind += increment
    return res


# def main():
#     print(slide_window(list(range(18)),5,2))
#     return 0

# main()