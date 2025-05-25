from itertools import compress,accumulate
from math import sqrt
import operator
from collections import defaultdict

def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).

    You can assume that "number" is an integer at least equal to 2.

    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    # return 0
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    dict = defaultdict(int)
    for num in range(2,int(sqrt(number))+1):
    #for num in range(2,number+1):
        if number == 1:
            break
        while number % num == 0:
            dict[num] = dict[num]+1
            number = number//num
    #这个if是如果for循环只遍历到sqrt+1的结果，因为一个合数最多有一个大于sqrt的因数，这是数学性质。
    #如果遍历到n+1就不需要加这个if
    if number > 1:
        dict[number] = dict[number] + 1
    times = 1
    for x in dict:
        times = times * x
    return times

#sample answer
"""
    counter = defaultdict(int)
    for factor in range(2, number + 1):
        if number == 1:
            break
        while number % factor == 0:
            counter[factor] += 1
            number = number // factor
    # 返回连乘的乘积
    return prod(counter)
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
