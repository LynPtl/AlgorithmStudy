"""
"""
def loop(D, x):
    '''
    >>> loop({1: 1}, 0)
    >>> loop({1: 2, 2: 2}, 1)
    >>> loop({1: 2, 2: 3}, 1)
    >>> loop({1: 2, 2: 3, 3: 2}, 1)
    >>> loop({1: 1}, 1)    
    1--1
    >>> loop({1: 2, 2: 1}, 2)
    1--2--1
    >>> loop({12: 14, 13: 14, 14: 7, 7: 12, 6: 8, 8: 6, 5: 11}, 14)
    7--12--14--7
    >>> loop({0: 4, 1: 0, 2: 1, 3: 2, 4: 7, 5: 6, 6: 4, 7: 0, 8: 8, 9: 4}, 4)
    0--4--7--0
    >>> loop({0: 7, 1: 7, 2: 3, 3: 8, 4: 6, 5: 8, 6: 6, 7: 4, 8: 9, 9: 2}, 8)
    2--3--8--9--2
    '''
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    #sample answer
    visited = []
    result = None
    for k in sorted(D.keys()):
        if k not in visited:
            cycle = [k]
            while cycle[-1] in D:
                cycle.append(D[cycle[-1]])
                if cycle[-1] == cycle[0]:
                    visited.extend(cycle)
                    if x in cycle:
                        result = cycle[::]
                        break
                if cycle.count(cycle[-1]) == 2:
                    break
    if result:
        print("--".join(str(x) for x in result))


if __name__ == '__main__':
    import doctest
    doctest.testmod()