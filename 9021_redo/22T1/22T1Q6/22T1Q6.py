from collections import defaultdict

# The words in the file are supposed to consist of nothing but letters
# (no apostrophes, no hyphens...), possibly immediately followed by
# a single full stop, exclamation mark, question mark,
# comma, colon or semicolon.
#
# A sentence ends in a full stop, an exclamation mark or a question mark
# (neither in a comma nor in a colon nor in a semicolon).
#
# There can be any amount of space anywhere between words, before the
# first word, and after the last word.
#
# We do not distinguish between words that only differ in cases.
# For instance, millionaires, Millionaires, MILLIONAIRES are
# 3 variants of the same word.
#
# The enumeration of sentences starts with 1.
# Within a given sentence, the enumeration of words starts with 1.
#
# It should all happen naturally, but for a given spotted word:
# - Smaller sentence numbers come before larger sentence numbers.
# - For a given sentence, smaller word numbers come before
#   larger word numbers.
#
# You can assume that filename is the name of a file that exists
# in the working directory. Do NOT use absolute paths. 
#
# The code that is already written makes sure that spotted words
# are output in capitalised form, and in lexicographic order, so
# you do not have to take care of it.

def longest_words(filename):
    '''
    >>> longest_words('9021_redo/22T1/22T1Q6/edgar_poe_1.txt')
    Connoisseurship:
        Spotted as word number 6 in sentence number 10.
    >>> longest_words('9021_redo/22T1/22T1Q6/edgar_poe_2.txt')
    Retribution:
        Spotted as word number 6 in sentence number 4.
    Unredressed:
        Spotted as word number 4 in sentence number 4.
        Spotted as word number 4 in sentence number 5.
    >>> longest_words('9021_redo/22T1/22T1Q6/oscar_wild_1.txt')
    Establishment:
        Spotted as word number 9 in sentence number 1.
    Individualism:
        Spotted as word number 17 in sentence number 23.
    Sentimentally:
        Spotted as word number 12 in sentence number 9.
    >>> longest_words('9021_redo/22T1/22T1Q6/oscar_wild_2.txt')
    Incomparable:
        Spotted as word number 78 in sentence number 1.
        Spotted as word number 83 in sentence number 1.
    Intelligence:
        Spotted as word number 11 in sentence number 6.
    Surroundings:
        Spotted as word number 28 in sentence number 12.
    '''
    longest_words = defaultdict(list)
    line_nb = -1
    word_nb = -1
    # POSSIBLY MODIFY THE PREVIOUS TWO LINE AND INSERT YOUR CODE HERE
    counter = defaultdict(list)
    with open(filename) as file:
        content = file.read()
        start, end, line_nb = 0,0,0
        while end < len(content):
            if content[end] in "?!.":
                line_nb += 1
                line = content[start:end]
                new_line = line.strip()
                for item in line:
                    #如果不是字符
                    if not item.isalpha():
                        new_line = new_line.replace(item," ")
                word_nb = 0
                for word in new_line.strip().split():
                    word_nb += 1
                    counter[len(word)].append((word,line_nb,word_nb))
                start = end + 1
            end += 1
    if counter:
        max_length = max(counter.keys())
        for word,index,word_nb in counter[max_length]:
            longest_words[word.lower()].append((index,word_nb))



    for word in sorted(longest_words):
        print(f'{word.capitalize()}:')
        for (sentence_nb, word_nb) in longest_words[word]:
            print(f'    Spotted as word number {word_nb} in sentence '
                  f'number {sentence_nb}.'
                 )

    #正则版本
    import re
    longest_words = defaultdict(list)
    line_nb = -1
    word_nb = -1
    counter = defaultdict(list)
    with open(filename) as file:
        line_nb = 0
        for sentence in re.split(r"[|!\.]",file.read()):
            if sentence.isspace():
                continue
            line_nb += 1
            word_nb = 0
            for word in re.findall(r"\w+",sentence):
                if word.isspace():
                    continue
                word_nb += 1
                counter[len(word)].append((word,line_nb,word_nb))
    if counter:
        max_length = max(counter.keys())
        for word,index,word_nb in counter[max_length]:
            longest_words[word.lower()].append((index,word_nb))
    for word in sorted(longest_words.keys()):
        print(f"{word.capitalize()}:")
        for sentence_nb, word_nb in longest_words[word]:
            print(f'    Spotted as word number {word_nb} in sentence '
                  f'number {sentence_nb}.'
                )   

if __name__ == '__main__':
    import doctest
    doctest.testmod()
