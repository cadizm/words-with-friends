from collections import defaultdict
import string


def dictify(sequence):
    "map letter to num occurrences"
    res = defaultdict(int)

    for letter in sequence:
        res[letter] += 1

    return res


def lookupify(dictfile='/usr/share/dict/words'):
    "map n to words with length n"
    res = defaultdict(list)

    with open(dictfile) as f:
        for word in f:
            word = word.strip().lower()
            res[len(word)].append(word)

    return res


def dict_subset(needle, haystack):
    "return True if needle is a `dict subset' of haystack, False otherwise"

    for k in needle:
        if k not in haystack:
            return False
        else:
            haystack[k] -= needle[k]

        if haystack[k] < 0:
            return False

    return True


def find_words(letters, D=None):
    D = D or lookupify()
    res = set()

    for i in range(2, len(letters) + 1):
        for w in D[i]:
            # dictify faster than deepcopy
            if dict_subset(dictify(w), dictify(letters)):
                if w not in res:
                    res.add(w)
                    yield w


if __name__ == '__main__':
    try:
        import sys
        word = sys.argv[1]
    except:
        word = 'rottedi'
    letters = list(word)

    D = lookupify('enable1.txt')

    # only handles when blank for now
    if ' ' in word:
        words = []
        for letter in string.lowercase:
            words.append(word.replace(' ', letter))
    else:
        words = [word]

    for word in words:
        for w in find_words(word, D):
            print(len(w), w)
