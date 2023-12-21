
def remove_punctuation(test_str):
    # Using filter() and lambda function to filter out punctuation characters
    result = ''.join(filter(lambda x: x.isalpha() or x.isspace(), test_str))
    return result

def encode_codebook(fname):
    # Encode the codebook
    lineNo = 0
    codebk = {}
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            lineNo += 1
            line = remove_punctuation(line)
            eles = line.split(" ")
            wordNo = 0
            for ele in eles:
                if (ele.isalpha()):
                    wordNo += 1
                    word = ele.lower()
                    # codebk.get(word, []).append((lineNo, wordNo))
                    if (word in list(codebk.keys())):
                        codebk[word].append((lineNo, wordNo))
                    else:
                        codebk[word] = [(lineNo, wordNo)]
    return codebk

def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
    
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert type(message)==str
    assert type(fname)==str
    
    # Encode the codebook
    # print(codebk)
    codebk = encode_codebook(fname)
    # print(codebk["let"])
    # print(codebk["secret"])

    # Encode the text using the codebook
    sq = []
    words = list(message.split(" "))
    for i in words:
        il = i.lower()
        assert (il in codebk.keys()) # codebook has the key
        assert (codebk[il] != []) # code tuple not used up
        sq.append(codebk[il].pop())
    return sq


def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message. 
    
    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert type(fname)==str
    assert type(inlist)==list
    # print(list(set(inlist)))
    # print(inlist)
    assert len(list(set(inlist)))==len(inlist)
    codebk = encode_codebook(fname)
    msg = []
    for i in inlist:
        for key, value in codebk.items():
            if i in value:
                msg.append(key)
    assert len(msg)==len(inlist)
    return " ".join(msg)


# def main():
#     msg = "let us not say we met late at the night about the secret"
#     fn = "d.txt"
#     sq = encrypt_message(msg, fn)
#     mgg = decrypt_message(sq, fn)
#     print(sq)
#     print(msg)
#     print(mgg)
#     print(msg==mgg)
    
#     return 0


# main()