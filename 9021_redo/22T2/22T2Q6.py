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


def unknown_words(filename):
    '''
    >>> unknown_words('edgar_poe_1.txt')
    There are no unknown words of length greater than 2.
    >>> unknown_words('edgar_poe_2.txt')
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
    >>> unknown_words('oscar_wild_1.txt')
    There are no unknown words of length greater than 2.
    >>> unknown_words('oscar_wild_2.txt')
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
    # pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
    with open("dictionary.txt") as file1:
        dictionary = set()
        for line in file1:
            dictionary.add(line.strip().lower())
        
        unknown = defaultdict(set)
        with open(filename) as file:
            content = file.read()
            for item in content:
                if not item.isalpha():
                    content = content.replace(item,' ')
                words = content.split()
                for word in words:
                    if len(word)>2 and word.lower not in dictionary:
                        unknown[len].add(word.capitalize())
            if unknown:
                print("There are no unknown words of length greater than 2.")
                for key in sorted(unknown.keys()):
                    print(f"  - Of length {key}:")
                    for word in sorted(unknown[key]):
                        print(f"      {word}")
            else:
                print(f"There are no unknown words of length greater than 2.")
if __name__ == '__main__':
    import doctest
    doctest.testmod()
