# Will be tested only with number an integer.
#
# If number is positive, returns a positive integer.
# If number is negative, returns a negative integer.
#
# The digits of the returned integer are the digits of number
# ordered from largest to smallest.


def reorder(number):
    """
    >>> reorder(0)
    0
    >>> reorder(2)
    2
    >>> reorder(-33)
    -33
    >>> reorder(202)
    220
    >>> reorder(242242)
    442222
    >>> reorder(-3210123)
    -3322110
    >>> reorder(22659717106393887106)
    99887776665332211100
    """
    # return 0
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    if number == 0:
        return 0
    if number < 0:
        flag = False
    else:
        flag = True
    strn = str(abs(number))
    strn = sorted(strn)[::-1]
    if flag == False:
        return int('-'+"".join(strn))
    else:
        return int("".join(strn))
    
    #sample answer
    """
    n = int("".join(sorted(str(abs(number)),reverse=True)))
    return n if number > 0 else 0 - n
    """
if __name__ == "__main__":
    import doctest

    doctest.testmod()
