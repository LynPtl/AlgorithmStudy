# Final Exam Question 1

def count_of_given_digit_in_numbers_in_list(L, d):
    '''
    You can assume that L is a list of positive integers and d is a digit.
    
    >>> count_of_given_digit_in_numbers_in_list([3, 3333, 33], 3)
    7
    >>> count_of_given_digit_in_numbers_in_list([13, 14, 258], 9)
    0
    >>> count_of_given_digit_in_numbers_in_list([1, 21, 30, 1411], 1)
    5
    >>> count_of_given_digit_in_numbers_in_list([4082, 5395, 7888, 5697], 0)
    1
    >>> count_of_given_digit_in_numbers_in_list([4082, 5395, 7888, 5697], 1)
    0
    >>> count_of_given_digit_in_numbers_in_list([4082, 5395, 7888, 5697], 7)
    2
    >>> count_of_given_digit_in_numbers_in_list([4082, 5395, 7888, 5697], 8)
    4
    '''
    strL = ""
    count = 0
    for i in L:
        strL += str(i)
    for i in range(len(strL)):
        if strL[i] == str(d):
            count += 1
    return count
    # return
    # REPLACE return WITH YOUR CODE

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
