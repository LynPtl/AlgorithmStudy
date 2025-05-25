from random import seed, randint
import sys


# Given a number n, if n does not occur in the list L that has been
# generated, or if n is not the sum of two numbers that occur before
# some occurrence of n in L, then n is not recorded in R; otherwise,
# ONLY THE FIRST (LEFTMOST) occurrence of n in L that is the sum of two
# numbers that occur before in L is recorded in R.
#
# When an occurrence of a number n is recorded in R, we also record
# the unique pair (a, b) such that:
# - n = a + b,
# - a and b occur before in L, and
# - a occurs AS MUCH TO THE LEFT in L as possible.
def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 3, 0)
    Here is L: [0, 0, 0]
    The members of L that are sums of two previous terms is: [0]
    Here are all details:
        0: 0 + 0
    >>> f(0, 3, 1)
    Here is L: [1, 1, 0]
    The members of L that are sums of two previous terms is: []
    Here are all details:
    >>> f(0, 4, 1)
    Here is L: [1, 1, 0, 1]
    The members of L that are sums of two previous terms is: [1]
    Here are all details:
        1: 1 + 0
    >>> f(0, 5, 2)
    Here is L: [1, 1, 0, 1, 2]
    The members of L that are sums of two previous terms is: [1, 2]
    Here are all details:
        1: 1 + 0
        2: 1 + 1
    >>> f(1, 15, 3)
    Here is L: [1, 0, 2, 0, 3, 3, 3, 3, 1, 0, 3, 0, 3, 3, 0]
    The members of L that are sums of two previous terms is: [3, 1, 0]
    Here are all details:
        3: 1 + 2
        1: 1 + 0
        0: 0 + 0
    >>> f(0, 8, 4)
    Here is L: [3, 3, 0, 2, 4, 3, 3, 2]
    The members of L that are sums of two previous terms is: [3, 2]
    Here are all details:
        3: 3 + 0
        2: 0 + 2
    >>> f(1, 12, 8)
    Here is L: [2, 1, 4, 1, 7, 7, 7, 6, 3, 1, 7, 0]
    The members of L that are sums of two previous terms is: [6, 3, 7]
    Here are all details:
        6: 2 + 4
        3: 2 + 1
        7: 1 + 6
    >>> f(2, 15, 7)
    Here is L: [0, 1, 1, 5, 2, 4, 4, 3, 0, 2, 6, 6, 5, 7, 4]
    The members of L that are sums of two previous terms is: [1, 2, 4, 3, 6, 5, 7]
    Here are all details:
        1: 0 + 1
        2: 1 + 1
        4: 0 + 4
        3: 1 + 2
        6: 1 + 5
        5: 0 + 5
        7: 1 + 6
    >>> f(3, 20, 10)
    Here is L: [3, 9, 8, 2, 5, 9, 7, 10, 9, 1, 9, 0, 7, 4, 8, 3, 3, 7, 8, 8]
    The members of L that are sums of two previous terms is: [5, 7, 10, 9, 4, 8, 3]
    Here are all details:
        5: 3 + 2
        7: 2 + 5
        10: 3 + 7
        9: 2 + 7
        4: 3 + 1
        8: 3 + 5
        3: 3 + 0
    >>> f(4, 10, 20)
    Here is L: [7, 9, 3, 12, 15, 4, 2, 2, 0, 12]
    The members of L that are sums of two previous terms is: [12, 15]
    Here are all details:
        12: 9 + 3
        15: 3 + 12
    '''
    if nb_of_elements < 3:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    result = {}
    # INSERT SOME CODE HERE
    for k in range(2, len(L)):
        for i in range(k):
            for j in range(i + 1, k):
                if L[k] == L[i] + L[j] and L[k] not in R:
                    R.append(L[k])
                    result[L[k]] = (L[i], L[j])
                    break

    print('The members of L that are sums of two previous terms is:', R)
    print('Here are all details:')
    # INSERT SOME CODE HERE
    for item in R:
        print(f"    {item}: {result[item][0]} + {result[item][1]}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()