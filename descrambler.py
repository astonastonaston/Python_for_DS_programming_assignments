import itertools
import copy

# def load_dictionary():
#     # Load the dictionary from the provided file
#     file_path = 'tmp/google-10000-english-no-swears.txt'
#     word_map = {} # {length: set}

#     with open(file_path, 'r') as file:
#         for line in file:
#             word = line.strip()
#             length = len(word)
#             if length not in word_map:
#                 word_map[length] = set()
#             word_map[length].add(word)

#     return word_map

# def descrambler(w, k):
#     # Load a dictionary of valid words as a hash-map
#     valid_words_map = load_dictionary()

#     # Generate all possible combinations of words for each partition length
#     # print("0")
#     all_combinations = itertools.product(*(valid_words_map.get(length, set()) for length in k))
#     # print("1")
#     # all_combinations = set(all_combinations)
#     # print("2")
#     all_combinations = [combo for combo in all_combinations if sorted("".join(combo)) == sorted(w)]
#     # print("3")
#     for combo in all_combinations:
#         yield " ".join(combo)

def load_dictionary():
    # Load the dictionary from the provided file
    file_path = '/tmp/google-10000-english-no-swears.txt'
    word_map = {}  # {length: set}

    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            length = len(word)
            if length not in word_map:
                word_map[length] = set()
            word_map[length].add(word)

    return word_map

def descrambler_helper(remaining, lengths, current, valid_words_map):
    if not remaining:
        yield ' '.join(current)
        return
    # print(len(current))
    # print(remaining)
    length = lengths[len(current)]
    for word in valid_words_map.get(length, set()):
        # check if word is in the remaining string
        remaining_cp = copy.copy(remaining)
        in_flag = True
        for x in word:
            if (x in remaining_cp):
                remaining_cp = remaining_cp.replace(x, "", 1)
            else:
                in_flag = False
                break
        if in_flag:
            # print("word:")
            # print(word)
            yield from descrambler_helper(remaining_cp, lengths, current + [word], valid_words_map)

def descrambler(w, k):
    # Load a dictionary of valid words as a hash-map
    valid_words_map = load_dictionary()
    lengths = k

    # Start the recursion
    yield from descrambler_helper(w, lengths, [], valid_words_map)

# Example usage:
# result = list(descrambler('trleeohelh', (5, 5)))
# print(result)

# result = list(descrambler('choeounokeoitg', (3, 5, 6)))
# print(result)

# result = list(descrambler('qeodwnsciseuesincereins', (4, 7, 12)))
# print(result)
