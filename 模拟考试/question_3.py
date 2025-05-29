# Will be tested only with number an integer.
#
# If number is positive, returns a positive integer.
# If number is negative, returns a negative integer.
#
# The digits of the returned integer are the digits of odd number
# ordered from largest to smallest.

def transform(number):
    '''
    >>> transform(0)
    0
    >>> transform(2)
    0
    >>> transform(-33)
    -33
    >>> transform(101)
    11
    >>> transform(-101)
    -11
    >>> transform(202)
    0
    >>> transform(-202)
    0
    >>> transform(242242)
    0
    >>> transform(1357913)
    9753311
    >>> transform(-3210123)
    -3311
    >>> transform(22659717106393887106)
    99777533111
    '''
    # return 0
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    if number == 0:
        return 0
    if number > 0:
        is_positive = True
    else:
        is_positive = False
    strn = str(abs(number))
    for i in "02468":
        strn = strn.replace(i,"")
    listn = []
    for i in range(len(strn)):
        if strn[i] != "":
            listn.append(strn[i])
    listn = sorted(listn,reverse=True)
    if not listn:
        return 0
    if is_positive:
        return int("".join(listn))
    else:
        return 0-int("".join(listn))

if __name__ == '__main__':
    import doctest
    doctest.testmod()