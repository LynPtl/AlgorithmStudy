dictionary_file = 'dictionary.txt'

def number_of_words_in_dictionary(word_1, word_2):
    '''
    "dictionary.txt" is stored in the working directory.

    >>> number_of_words_in_dictionary('company', 'company')
    Could not find company in dictionary.
    >>> number_of_words_in_dictionary('company', 'comparison')
    Could not find at least one of company and comparison in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'comparison')
    Could not find at least one of COMPANY and comparison in dictionary.
    >>> number_of_words_in_dictionary('company', 'COMPARISON')
    Could not find at least one of company and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPANY')
    COMPANY is in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPARISON')
    COMPARISON is in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPARISON')
    Found 14 words between COMPANY and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPANY')
    Found 14 words between COMPARISON and COMPANY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIOUSLY')
    Found 2 words between CONSCIOUS and CONSCIOUSLY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIENTIOUS')
    Found 3 words between CONSCIOUS and CONSCIENTIOUS in dictionary.
    '''
    # print()
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    words = []
    index1 = index2 = -1
    with open('9021_redo/dictionary.txt') as file:
        for word in file:
            words.append(word.strip())
    for i in range(len(words)):
        if words[i] == word_1:
            index1 = i
        if words[i] == word_2:
            index2 = i
    if word_1 == word_2 and index1 != -1:
        print(f"{word_1} is in dictionary.")
        return
    if word_1 == word_2 and index1 == -1:
        print(f"Could not find {word_1} in dictionary.")
        return
    result = abs(index1-index2)+1
    if index1 == index2 == -1:
        print(f"Could not find at least one of {word_1} and {word_2} in dictionary.")
        return
    if index1 != -1 and index2 != -1:
        print(f"Found {result} words between {word_1} and {word_2} in dictionary.")
        return
    if index1 != -1 and index2 == -1:
        print(f"{word_1} is in dictionary.")
        return
    if index1 == -1 and index2 != -1:
        print(f"{word_2} is in dictionary.")
        return
    return
#sample answer
#使用index方法可以大幅简化
"""
    words = []
    with open('dictionary.txt') as file:
        for line in file:
            words.append(line.strip())

    if word_1 == word_2:
        if word_1 in words:
            print(f"{word_1} is in dictionary.")
        else:
            print(f"Could not find {word_1} in dictionary.")
    else:
        if word_1 in words and word_2 in words:
            gap = abs(words.index(word_1) - words.index(word_2)) + 1
            print(f"Found {gap} words between {word_1} and {word_2} in dictionary.")
        else:
            print(f"Could not find at least one of {word_1} and {word_2} in dictionary.")
"""
if __name__ == '__main__':
    import doctest

    doctest.testmod()
