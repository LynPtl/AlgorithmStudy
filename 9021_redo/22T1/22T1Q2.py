from random import seed, randint
from collections import defaultdict
import sys


# R is the list of lists of members of L that all end in the same digit,
# with duplicates removed,
# - longer lists coming before shorter lists,
# - the list associated with m as last digit coming before
#   the list associated with n as last digit if both lists
#   have the same length and m > n,
# - within a given list,
#   - longer numbers (as measured by their number of digits) coming before
#     shorter numbers,
#   - numbers of the same length keeping the order of
#     their first occurrences within L.
#
# For instance, take L equal to
# [26, 1, 66, 94, 4, 20, 30, 2, 7, 87, 18, 88, 47]
# - Three numbers end in 7, whereas only two numbers end in 6,
#   which explains why [87, 47, 7] comes before [26, 66] in R.
# - Two numbers end in 6 and two numbers end in 4; also, 6 is greater
#   than 4, which explains why [26, 66] comes before [94, 4] in R.
# - 87 and 47 have two digits, where 7 has only one digit,
#   which explains why 87 and 47 come before 7 in [87, 47, 7].
# - The first (unique in this case) occurrence of 87 comes before
#   the first (unique in this case) occurrence of 47 in L,
#   which explains why 87 comes before 47 in [87, 47, 7].

def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(1, 12, 1)
    Here is L: [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0]
    Here is R: [[1], [0]]
    >>> f(3, 15, 8)
    Here is L: [3, 8, 2, 5, 7, 1, 0, 7, 4, 8, 3, 3, 7, 8, 8]
    Here is R: [[8], [7], [5], [4], [3], [2], [1], [0]]
    >>> f(6, 12, 50)
    Here is L: [50, 36, 5, 31, 48, 16, 2, 0, 9, 42, 37, 30]
    Here is R: [[50, 30, 0], [36, 16], [42, 2], [9], [48], [37], [5], [31]]
    >>> f(9, 8, 5000)
    Here is L: [3792, 3058, 2188, 1134, 1524, 52, 2771, 4118]
    Here is R: [[3058, 2188, 4118], [1134, 1524], [3792, 52], [2771]]
    >>> f(12, 15, 30)
    Here is L: [15, 8, 21, 16, 21, 11, 4, 12, 0, 11, 15, 8, 20, 25, 14]
    Here is R: [[15, 25], [14, 4], [21, 11], [20, 0], [8], [16], [12]]
    >>> f(15, 13, 100)
    Here is L: [26, 1, 66, 94, 4, 20, 30, 2, 7, 87, 18, 88, 47]
    Here is R: [[87, 47, 7], [18, 88], [26, 66], [94, 4], [20, 30], [2], [1]]
    '''
    if nb_of_elements < 1:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    # INSERT YOUR CODE HERE
    dict = defaultdict(list)
    for item in L:
        if item not in dict[item % 10]:
            dict[item % 10].append(item)
    for key,values in sorted(dict.items(), key = lambda items : (len(items[1]),items[0]),reverse=True):
        # 第61这一行的lambda不是很好写 这个items[0]对应的是key，items[1]对应的是value
        # 先以长度进行排列，长度相等的以末尾数字大小进行排列
        values = sorted(values, key = lambda item : len(str(item)),reverse=True)
        # 对于每个小数组，内部按照长度进行排列
        R.append(values)
    print('Here is R:', R)
if __name__ == '__main__':
    import doctest

    doctest.testmod()