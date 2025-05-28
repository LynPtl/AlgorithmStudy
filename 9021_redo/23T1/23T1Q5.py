# Given two sets sums and summands of integers and an integer a,
# computes the LONGEST lists of the form
# [a, a + n_1, a + n_1 + n_2, ..., a + n_1 + n_2 + ... + n_k]
# such that:
# - a, a + n_1, a + n_1 + n_2, ..., a + n_1 + n_2 + ... + n_k are all in sums;
# - n_1, n_2, ..., n_k are all in summands and DISTINCT.
#
# The code is already written to print out the lists in lexicographic order
# (together with extra information on how they have been obtained).
#
# You can assume that the function is called with sets of integers
# as first two arguments and with an integer as third argument. 


def chains(sums, summands, a):
    '''
    >>> chains({}, {1, 2, 3}, 1)
    >>> chains({1, 2, 3}, {}, 4)
    >>> chains({1, 2, 3}, {}, 2)
    [2]
    >>> chains({11, 12, 13, 14, 15, 16}, {1, 2, 3, 4}, 11)
    [11, 12, 14] by successively adding 1, 2
    [11, 12, 15] by successively adding 1, 3
    [11, 12, 16] by successively adding 1, 4
    [11, 13, 14] by successively adding 2, 1
    [11, 13, 16] by successively adding 2, 3
    [11, 14, 15] by successively adding 3, 1
    [11, 14, 16] by successively adding 3, 2
    [11, 15, 16] by successively adding 4, 1
    >>> chains({1, 3, 4, 6, 9, 10, 20}, {-30, 1, 2, 3, 5, 6, 30}, 3)
    [3, 4, 6, 9] by successively adding 1, 2, 3
    >>> chains({10, 12, 13, 14, 16, 21, 26, 36, 37, 38, 50},\
               {2, 4, 7, 10, 16, 20, 100}, 10)
    [10, 12, 16, 26] by successively adding 2, 4, 10
    [10, 12, 16, 36] by successively adding 2, 4, 20
    [10, 14, 16, 26] by successively adding 4, 2, 10
    [10, 14, 16, 36] by successively adding 4, 2, 20
    [10, 14, 21, 37] by successively adding 4, 7, 16
    [10, 26, 36, 38] by successively adding 16, 10, 2
    '''

    for L in sorted(_chains(sums, summands, a)):
        if len(L) == 1:
            print(L)
        else:
            print(L, 'by successively adding',
                  ', '.join(str(L[i + 1] - L[i])
                                for i in range(len(L) - 1)
                           )
                 )
# sample answer
def _chains(sums, summands, a):
    # return []
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    from itertools import permutations
    from collections import defaultdict
    solutions = []
    if a in sums:
        counter = defaultdict(set)
        counter[1].add(tuple([a]))
        if summands:
            for items in permutations(summands,len(summands)):
                sub_list = [a]
                for num in items:
                    if sub_list[-1] + num in sums:
                        sub_list.append(sub_list[-1] + num)
                    else:
                        break
                counter[len(sub_list)].add(tuple(sub_list))
        longest = max(counter)
        solutions = map(list, counter[longest])
    return solutions


if __name__ == '__main__':
    import doctest
    doctest.testmod()
