from urllib.request import urlopen
u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
response = urlopen(u)
words = [i.strip().decode('utf8') for i in response.readlines()]
# print(words)

def get_average_word_length(words):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert type(words)==list
    return sum([len(i) for i in words]) / len(words)

def get_longest_word(words):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert type(words)==list
    return max(words, key=lambda x: len(x)) 

def get_longest_words_startswith(words,start):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert type(words)==list
    return max(words, key=lambda x: len(x) if x.startswith(start) else 0) 

def get_most_common_start(words):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert type(words)==list
    les = {}
    for i in words:
        if (les.get(i[0]) == None):
            les[i[0]] = 1
        else:
            les[i[0]] += 1
    return max(les, key=lambda x: les.get(x))

def get_most_common_end(words):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert type(words)==list
    les = {}
    for i in words:
        if (les.get(i[-1]) == None):
            les[i[-1]] = 1
        else:
            les[i[-1]] += 1
    return max(les, key=lambda x: les.get(x)) # in dict, each lambdaed term is the key

def write_chunks_of_five(words,fname):
    """
    Input: Data and output file name\n
    Return: Word chunks
    """
    assert type(words)==list
    assert type(fname)==str

    f = open(fname, 'w', newline ='')
    for i in range(0, len(words), 5):
        # print([float("{:.2f}".format(data_value)), float("{:.2f}".format(data_value**2)), round((data_value+data_value**2)/3, 2)])
        f.write(" ".join(words[i: min(i+5, len(words))]) + "\n")
    f.close()
    return 0


# def main():
#     # print(words)
#     print(get_average_word_length(words))
#     print(get_longest_word(words))
#     print(get_longest_words_startswith(words, start='a'))
#     print(get_most_common_end(words))
#     print(get_most_common_start(words))
#     write_chunks_of_five(words, "bello.csv")
#     return 0

# main()