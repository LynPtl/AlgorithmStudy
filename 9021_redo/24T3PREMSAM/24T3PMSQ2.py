#  Returns an integer whose first digit is "number"'s first digit,
#  and whose other digits are those in "number" plus "by" modulo 10
#  ("by" is set to 1 by default).

#  You can assume that "number" is a valid strictly positive integer
#  and "by" is a valid integer.

def shift(number, by = 1):
    '''   
    >>> shift(8)
    8
    >>> shift(18901)
    19012
    >>> shift(932054, 0)
    932054
    >>> shift(20123, -1)
    29012
    >>> shift(310293, 2)
    332415
    >>> shift(4250328, -3)
    4927095
    >>> shift(55439012, 4)
    59873456
    >>> shift(692810, -15)
    647365
    >>> shift(7021324, 26)
    7687980
    '''
    # Insert your code here (the output is returned, not printed out)               
    strn = str(number)
    result = strn[0]
    for i in range(1,len(strn)):
        result += str((int(strn[i]) + by) % 10)
    return int(result)
    #sample answer
    """
    n = str(number)
    result = n[0]
    for second in n[1:]:
        result += str((int(second) + by) % 10)
    return int(result)
    """
if __name__ == '__main__':
    import doctest
    doctest.testmod()
