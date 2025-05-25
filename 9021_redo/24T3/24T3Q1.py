def f(n):
    """
    >>> f(1)
    ((1,), (1,))
    >>> f(2)
    ((1, 2), (2, 1))
    >>> f(3)
    ((1, 2, 4), (4, 2, 1))
    >>> f(4)
    ((1, 2, 4, 7), (7, 4, 2, 1))
    >>> f(5)
    ((1, 2, 4, 7, 11), (11, 7, 4, 2, 1))
    >>> f(6)
    ((1, 2, 4, 7, 11, 16), (16, 11, 7, 4, 2, 1))
    >>> f(7)
    ((1, 2, 4, 7, 11, 16, 22), (22, 16, 11, 7, 4, 2, 1))
    >>> f(8)
    ((1, 2, 4, 7, 11, 16, 22, 29), (29, 22, 16, 11, 7, 4, 2, 1))
    """
    if n == 1:
        return ((1,),(1,))
    list1 = []
    for i in range(n):
        if i == 0:
            list1.append(1)
        else:
            list1.append(list1[-1] + i)
    return (tuple(list1),tuple(list(reversed(list1))))
    #sample answer
    """
    count = 1
    res = []
    for i in range(n):
        count += 1
        res.append(count)
    return tuple(res),tuple(reversed(res))
    """
if __name__ == "__main__":
    import doctest

    doctest.testmod()
