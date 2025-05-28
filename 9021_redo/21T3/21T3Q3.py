'''
You might find the ord() function useful.
'''
def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of nothing but lowercase letters.
    
    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwrstuvabcde')
    'rstuv'
    '''
    maxl = 0
    result = ""
    if not word:
        return ''
    length = len(word)
    for i in range(length):
        cur = word[i]
        for j in range(i + 1, length):
            if ord(word[j]) == ord(cur[-1]) + 1:
                cur += word[j]
            else:
                break
        if len(cur) > maxl:
            result = cur
            maxl = len(cur)
    return result
    #sample answer
    """
    longest = ""
    if word:
        longest = sub_str = first = word[0]
        for second in word[1:]:
            if ord(first) + 1 == ord(second):
                sub_str += second
                if len(longest) < len(sub_str):
                    longest = sub_str
            else:
                sub_str = second
            first = second
    return longest
    """
    # REPLACE return WITH YOUR CODE
                



if __name__ == '__main__':
    import doctest
    doctest.testmod()

