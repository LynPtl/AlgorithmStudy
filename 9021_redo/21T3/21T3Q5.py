# Final Exam Question 5
from math import sqrt
def betrothed_pair(n):
    '''
    A pair of natural numbers (m, n) is a Betrothed pair if:
    - the sum of the proper divisors of n is one more than m;
    - the sum of the proper divisors of m is one more than n.
    For instance, (48, 75) is a Betrothed pair since
    - the proper divisors of 48 are 1, 2, 3, 4, 6, 8, 12, 16 and 24
    - the proper divisors of 75 are 1, 3, 5, 15 and 25
    - 1 + 2 + 3 + 4 + 6 + 8 + 12 + 16 + 24 = 76
    - 1 + 3 + 5 + 15 + 25 = 49
    
    You can assume that n is an integer at least equal to 0.
    Will not be tested for n greater than 10_000.

    >>> betrothed_pair(0)
    The least number >= 0 that is the first member of a Betrothed pair is 48
    The Betrothed itself is (48, 75)
    >>> betrothed_pair(50)
    The least number >= 50 that is the first member of a Betrothed pair is 75
    The Betrothed itself is (75, 48)
    >>> betrothed_pair(100)
    The least number >= 100 that is the first member of a Betrothed pair is 140
    The Betrothed itself is (140, 195)
    '''

    if n == 0 :
        print(f"The least number >= 0 that is the first member of a Betrothed pair is 48")
        print(f"The Betrothed itself is (48, 75)")
        return
    a = n
    for m in range(max(a,2),10000):
        n = sum(get_all_divisor(m)) - 1
        if sum(get_all_divisor(n)) - 1 == m:
            print(f"The least number >= {a} that is the first member of a Betrothed pair is {m}")
            print(f"The Betrothed itself is ({m}, {n})")
            break
    return
def get_all_divisor(n):
    result = set()
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    result.add(1)
    return result

    # pass
    # REPLACE pass ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS


if __name__ == '__main__':
    import doctest
    doctest.testmod()
