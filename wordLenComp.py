def compute_average_word_length(instring,unique=False):
    """
    Input: input string and the unique flag indicating whether counting once only\n
    Return: input words' average length
    """
    assert (type(instring)==str)
    assert (type(unique)==bool)
    sentences = [x for x in instring.split('\n') if (x != '')]
    wordDic = {}
    wordList, wordLen = [], []
    for s in sentences:
        words = [x for x in s.split(" ") if (x != '')]
        print(words)
        for w in words:
            if unique:
                wUpper = w.upper()
                if (wUpper not in wordDic.keys()):
                    wordDic[wUpper] = len(w)
            else:
                wordList.append(w)
                wordLen.append(len(w)) 

    print(wordList, wordLen, wordDic)
    if unique:
        return sum(wordDic.values()) / len(wordDic)
    else:
        return sum(wordLen) / len(wordLen)


# def main():
#     # print(compute_average_word_length(2,3))
#     # print(compute_average_word_length("Hello world\nworld Hello man", False))
#     # print(compute_average_word_length("Hello world\nworld Hello man", True))
#     print(compute_average_word_length("Mary had a little lamb \nits fleece was white as snow \nand everywhere that Mary went \nthe lamb was sure to go", False))
#     print(compute_average_word_length("Mary had a little lamb \nits fleece was white as snow \nand everywhere that Mary went \nthe lamb was sure to go", True))
#     return 0

# main()