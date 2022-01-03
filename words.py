from collections import defaultdict
import string


def occ(sequence):
    "Map char in sequence to its num of occurrences"
    res = defaultdict(int)

    for letter in sequence:
        res[letter] += 1

    return res


def lookupify(dictfile):
    "Map n to list of words of length n"
    res = defaultdict(list)

    with open(dictfile) as f:
        for word in f:
            word = word.strip().lower()
            res[len(word)].append(word)

    return res


def has_occ(needle, haystack):
    """
    Return true if for each key in needle:
        haystack[key] >= needle[key]

    Return False otherwise
    """

    for k in needle:
        if k not in haystack or haystack[k] < needle[k]:
            return False

    return True


table = lookupify('enable1.txt')


def find_words(letters):
    global table
    res = set()

    for i in range(2, len(letters) + 1):
        for w in table[i]:
            # occ faster than deepcopy
            if has_occ(occ(w), occ(letters)):
                res.add((len(w), w))

    return sorted(res, key=lambda x:(x[0], x[1]))


if __name__ == '__main__':
    try:
        import sys
        word = sys.argv[1]
    except:
        word = 'rottedi'

    letters = list(filter(lambda x: x != ' ', word))
    blanks = len(word) - len(letters)

    for n, w in find_words(letters):
        print(n, w)
