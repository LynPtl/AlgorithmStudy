import sys
from math import sqrt
from itertools import compress

from itertools import chain

def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    map = [True]*(n+1)
    map[0] = False
    map[1] = False
    for i in range(2,int(sqrt(n))+1):
        if map[i] == True:
            for j in range(i*i,n+1,i):
                map[j] = False
    for i in range(n-1,0,-1):
        if map[i] == True:
            print(f"The largest prime strictly smaller than {n} is {i}.")
            break

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

    
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    primes = sieve_of_primes_up_to(n - 1)
    print(f"The largest prime strictly smaller than {n} is {primes[-1]}.")
    """
if __name__ == '__main__':
    import doctest
    doctest.testmod()
