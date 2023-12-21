def convert_hex_to_RGB(hexList):
    """
    Input: A Hex code list\n
    Return: Decimal RGB values
    """
    assert (type(hexList) == list)
    assert (len(hexList) > 0)
    valList = []
    for hex in hexList:
        hex = int(hex[1:], 16)
        colTup = []
        for i in range(3):
            colTup.append((hex >> 8*(2-i)) & 0xFF) 
        colTup = tuple(colTup)
        valList.append(colTup)
    return valList


# def main():
#     print(convert_hex_to_RGB(['#FFAABB']))
#     print(convert_hex_to_RGB(['#FFAABB', '#09DDCC']))
#     return 0

# main()