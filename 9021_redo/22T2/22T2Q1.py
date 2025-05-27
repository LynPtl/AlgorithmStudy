# A sequence of identical digits is collapsed to one digit
# in the returned integer.
#
# You can assume that the function is called with an integer
# as argument.


def collapse(number):
    '''
    >>> collapse(0)
    0
    >>> collapse(-0)
    0
    >>> collapse(9)
    9
    >>> collapse(-9)
    -9
    >>> collapse(12321)
    12321
    >>> collapse(-12321)
    -12321
    >>> collapse(-1111222232222111)
    -12321
    >>> collapse(1155523335551116111666)
    152351616
    >>> collapse(-900111212777394440300)
    -9012127394030
    '''
    # return 0
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    strn = str(number)
    result = ""
    for i in range(0,len(strn)-1):
        if strn[i] != strn[i+1]:
            result += strn[i]
    result += strn[-1]
    return int(result)
    #sample answer
    """
    n = str(abs(number))
    if n:
        result = n[0]
        for cur in n[1:]:
            if result[-1] == cur:
                continue
            else:
                result += cur
    if number >= 0:
        return int(result)
    else:
        return 0-int(result)
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
