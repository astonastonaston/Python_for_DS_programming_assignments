def is_string_integer(strc):
    """
    Input: A character\n
    Return: True/False indicating whether the input is a decimal digit
    """
    assert type(strc) == str
    assert len(strc) == 1
    return strc.isdigit()


# def main():
#     print(is_string_integer('1'))
#     # print(is_string_integer('22'))
#     # print(is_string_integer('as2'))
#     print(is_string_integer('a'))
#     return 0

# main()