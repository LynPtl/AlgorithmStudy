def f(L):
    """
    >>> f([])
    []
    >>> f([1])
    [1]
    >>> f([1, 2])
    [1, 2]
    >>> f([1, 2, 3])
    [2, 3, 1]
    >>> f([1, 2, 3, 4])
    [2, 3, 1, 4]
    >>> f([1, 2, 3, 4, 5])
    [3, 4, 2, 5, 1]
    >>> f([1, 2, 3, 4, 5, 6])
    [3, 4, 2, 5, 1, 6]
    >>> f([1, 2, 3, 4, 5, 6, 7])
    [4, 5, 3, 6, 2, 7, 1]
    >>> f([-8, 6, 33, 0, 6, 5, 18, 14])
    [0, 6, 33, 5, 6, 18, -8, 14]
    >>> f([-8, 6, 33, 0, 6, 5, 18, 14, 5])
    [6, 5, 0, 18, 33, 14, 6, 5, -8]
    """
    #如果是偶数，那么先取中间的两个，然后左指针-1 右指针+1 先读左后读右
    #如果是奇数 先取中间的那一个，然后左指针-1 右指针+1，先读右后读左
    #比如有六个 012345 那么开始的指针就是23 分别是6/2和6/2-1
    #比如有五个 01234 那么开始的指针就是5//2
    answer = []
    length = len(L)
    if length == 0 or length == 1:
        return L
    if length % 2 == 0:
        left = length//2 - 1
        right = length//2
        offset = 0
        while offset + right < length:
            answer.append(L[left-offset])
            answer.append(L[right+offset])
            offset += 1
        return answer
    else:
        middle = length//2
        answer = [L[middle]]
        offset = 1
        while offset + middle < length:
            answer.append(L[middle+offset])
            answer.append(L[middle-offset])
            offset += 1
        return answer
if __name__ == "__main__":
    import doctest

    doctest.testmod()
