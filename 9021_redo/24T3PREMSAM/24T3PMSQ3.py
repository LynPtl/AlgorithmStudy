#  list_of_lists being a list of n lists of length l_1, ..., l_n,
#  returns a list of n lists of length l_1, ..., l_n consisting of
#  all elements in list_of_lists ordered from smallest to largest.

#  You can assume that list_of_lists is a list of lists of integers.


def redistribute(list_of_lists):
    """
    >>> redistribute([[]])
    [[]]
    >>> redistribute([[3, 1, 10, 5, 1, 10, 8]])
    [[1, 1, 3, 5, 8, 10, 10]]
    >>> redistribute([[2], [1], [2], [4]])
    [[1], [2], [2], [4]]
    >>> redistribute([[3, 40], [0], [7]])
    [[0, 3], [7], [40]]
    >>> redistribute([[32], [3, 40, 7], [40, 11]])
    [[3], [7, 11, 32], [40, 40]]
    >>> redistribute([[97, 21], [65], [9, 25, 24], [64], [73, 38, 98, 50]])
    [[9, 21], [24], [25, 38, 50], [64], [65, 73, 97, 98]]
    """
    # Insert your code here (the output is returned, not printed out)
    length = []
    allelements = []
    result = []
    for l in list_of_lists:
        length.append(len(l))
        allelements.extend(l)
    allelements = sorted(allelements)
    temp = 0
    for i in length:
        cur = []
        for j in range(i):
            cur.append(allelements[temp])
            temp += 1
        result.append(cur)
    return result

"""
    #sample answer
    L = sorted(x for sub_list in list_of_lists for x in sub_list)
    R = []
    if L:
        i = 0
        for sub_list in list_of_lists:
            R.append(L[i: i + len(sub_list)])
            i += len(sub_list)
    else:
        R.append([])
    return R

    # another version
    digits = []
    # 都添加到一个元素里面
    for nums in list_of_lists:
        digits.extend(nums)
    # 做一个排序
    digits.sort()
    result = []
    length = 0
    # 重新根据长度添加
    for nums in list_of_lists:
        result.append(digits[length : length + len(nums)])
        length += len(nums)
    return result
"""

if __name__ == "__main__":
    import doctest

    doctest.testmod()
