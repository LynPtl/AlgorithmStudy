from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The decomposition of L into increasing sublists is: []
    >>> f(0, 1, 10)
    Here is L: [6]
    The decomposition of L into increasing sublists is: [[6]]
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The decomposition of L into increasing sublists is: [[6], [6]]
    >>> f(1, 2, 10)
    Here is L: [2, 9]
    The decomposition of L into increasing sublists is: [[2, 9]]
    >>> f(0, 3, 10)
    Here is L: [6, 6, 0]
    The decomposition of L into increasing sublists is: [[6], [6], [0]]
    >>> f(1, 4, 10)
    Here is L: [2, 9, 1, 4]
    The decomposition of L into increasing sublists is: [[2, 9], [1, 4]]
    >>> f(20, 5, 10)
    Here is L: [10, 2, 4, 10, 10]
    The decomposition of L into increasing sublists is: [[10], [2, 4, 10], [10]]
    >>> f(1, 10, 20)
    Here is L: [4, 18, 2, 8, 3, 15, 14, 15, 20, 12]
    The decomposition of L into increasing sublists is: [[4, 18], [2, 8], [3, 15], [14, 15, 20], [12]]
    '''
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    # Insert your code here
    final = []
    if L:
        cur = [L[0]]
        curnum = L[0]
        for i in range(1,len(L)):
            if L[i] > curnum:
                cur.append(L[i])
            else:
                final.append(cur)
                cur = [L[i]]
            curnum = L[i]
        final.append(cur)
    print(f"The decomposition of L into increasing sublists is: {final}")
    #sample answer
"""
    R = []
    if L:
        R.append([L[0]])
        for i in range(1, len(L)):
            if L[i] > L[i - 1]:
                R[-1].append(L[i])
            else:
                R.append([L[i]])
    print(f"The decomposition of L into increasing sublists is: {R}")
"""
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
