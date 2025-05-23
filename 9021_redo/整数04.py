
def rearrange(number):
    '''
    Returns an integer consisting of all nonzero digits in "number",
    from smallest to largest.

    You can assume that "number" is a valid strictly positive integer.
    
    >>> rearrange(1)
    1
    >>> rearrange(200)
    2
    >>> rearrange(395)
    359
    >>> rearrange(10029001)
    1129
    >>> rearrange(301302004)
    12334
    >>> rearrange(9409898038908908934890)
    33448888889999999
    '''
    # return -1
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    strnum = str(number)
    result = []
    rstr = ""
    for i in strnum:
        if i != '0':
            result.append(i)
    result = sorted(result)
    for i in result:
        rstr = rstr + i
    print(int(rstr))

    #sample answer
    #return int("".join(sorted(str(number))))
    #运用整型int的特性，前导的0会全部忽略
    #因为sorted()的返回值是一个列表，因而要用join来进行格式化为str后转为int

if __name__ == '__main__':
    import doctest
    doctest.testmod()
