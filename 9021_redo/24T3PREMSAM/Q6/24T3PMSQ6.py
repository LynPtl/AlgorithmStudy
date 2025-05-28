# The words in the file are supposed to consist of nothing but letters
# (no apostrophes, no hyphens...), possibly immediately followed by
# a single full stop, exclamation mark, question mark,
# comma, colon or semicolon.
#
# There can be any amount of space anywhere between words, before the
# first word, and after the last word.
#
# We do not distinguish between words that only differ in cases.
# For instance, millionaires, Millionaires, MILLIONAIRES are
# 3 variants of the same word.
#
# You can assume that filename is the name of a file that exists
# in the working directory. Do NOT use an absolute path.
#
# The words of length greater than 2 are checked against the contents
# of dictionary.txt, also assumed to be stored in the working directory.
# Here too, do NOT use an absolute path.
#
# Unknown words (that is, words of length greater than 2 that are
# not found in dictionary.txt) are output only once, in capitalised form,
# in lexicographic order for each group, a group consisting of words
# all of the same length.
# Groups for shorter words are output before groups for longer words.

# Note that no tab is output anywhere, just single spaces.


from collections import defaultdict
import re

def unknown_words(filename):
    '''
    >>> unknown_words('9021_redo/24T3PREMSAM/Q6/edgar_poe_1.txt')
    There are no unknown words of length greater than 2.
    >>> unknown_words('9021_redo/24T3PREMSAM/Q6/edgar_poe_2.txt')
    There are unknown words of length greater than 2.
      - Of length 8:
          Practise
      - Of length 9:
          Fortunato
          Imposture
          Redresser
      - Of length 10:
          Immolation
      - Of length 11:
          Unredressed
      - Of length 12:
          Definitively
      - Of length 14:
          Definitiveness
      - Of length 15:
          Connoisseurship
    >>> unknown_words('9021_redo/24T3PREMSAM/Q6/oscar_wild_1.txt')
    There are no unknown words of length greater than 2.
    >>> unknown_words('9021_redo/24T3PREMSAM/Q6/oscar_wild_2.txt')
    There are unknown words of length greater than 2.
      - Of length 5:
          Renan
      - Of length 7:
          Realise
      - Of length 8:
          Flaubert
      - Of length 10:
          Neighbours
      - Of length 11:
          Misdirected
    '''
    pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
    unknown_counter = defaultdict(set)
    dictionary = set()
    with open("9021_redo/24T3PREMSAM/Q6/dictionary.txt") as file:
        for line in file:
            dictionary.add(line.strip())
    with open(filename) as file:
        sentences = re.split(r"[\?\.;!:]",file.read())
        for sentence in sentences:
            words = re.findall(r"\w+",sentence)
            for word in words:
                if len(word) > 2 and word.upper() not in dictionary:
                    unknown_counter[len(word)].add(word.capitalize())
    if not unknown_counter:
        print(f"There are no unknown words of length greater than 2.")
        return
    else:
        print(f"There are unknown words of length greater than 2.")
        for i in sorted(unknown_counter.keys()):
            print(f"  - Of length {i}:")
            for value in sorted(unknown_counter[i]):
                print(f"      {value}")
        return

if __name__ == '__main__':
    import doctest
    doctest.testmod()

