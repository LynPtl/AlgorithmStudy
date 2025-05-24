import sys
from itertools import compress
from math import sqrt

from itertools import chain


def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    # Insert your code here
    arr = [True]*(b+1)
    arr[0] = False
    arr[1] = False
    for i in range(2,int(sqrt(b))+1):
        if arr[i] == True:
            for j in range(i*i,b+1,i):
                arr[j] = False
    primes = []
    for i in range(a,b+1):
        if arr[i] == True:
            primes.append(i)
    
    for i in range(0,len(primes)-1):
        curgap = primes[i+1] - primes[i]
        max_gap = max(max_gap,curgap)
    
    if len(primes)<=1:
        max_gap = 1
    print(f"The maximum gap between successive prime numbers in that interval is {max_gap-1}")

#sample answer
"""
# 返回n以下所有的素数
def sieve_of_primes_up_to(n):
    sieve = list(range(2, n + 1))
    i = 0
    while sieve[i] <= round(n**0.5):
        sieve_as_set = set(sieve)
        k = 0
        while True:
            factor = sieve[i] * sieve[i + k]
            if factor > n:
                break
            sieve_as_set.remove(factor)
            k += 1
        sieve = sorted(sieve_as_set)
        i += 1
    return sieve

    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    # Insert your code here
    primes = sieve_of_primes_up_to(b)
    first = None
    for prime in primes:
        if prime >= a and first is None:
            first = prime
        if first is not None:
            max_gap = max(max_gap, prime - first - 1)
            first = prime
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
