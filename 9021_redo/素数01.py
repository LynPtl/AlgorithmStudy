import sys
from math import sqrt
from itertools import compress
from itertools import chain


def f(a, b):
    '''
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The number of prime numbers between 3 and 3 included is 1
    >>> f(4, 4)
    The number of prime numbers between 4 and 4 included is 0
    >>> f(2, 5)
    The number of prime numbers between 2 and 5 included is 3
    >>> f(2, 10)
    The number of prime numbers between 2 and 10 included is 4
    >>> f(2, 11)
    The number of prime numbers between 2 and 11 included is 5
    >>> f(1234, 567890)
    The number of prime numbers between 1234 and 567890 included is 46457
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    '''
    ###########
    '''
    count = 0
    for i in range(a,b+1):
        if is_prime(i):
            count += 1
    print(f"The number of prime numbers between {a} and {b} included is {count}")

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    '''
    ###########
# 以上是我写的完全超时做法
# 注意到大数，应该使用素筛法

    arr = [True]*(b+1)
    arr[0] = False
    arr[1] = False
    for i in range(2,int(sqrt(b))+1):
        if arr[i]:
            for j in range(i*i,b+1,i):
                arr[j] = False
    countb = 0
    counta = 0
    for i in range(len(arr)):
        if arr[i] == True:
            countb += 1
    for i in range(0,a):
        if arr[i] == True:
            counta += 1
    print(f"The number of prime numbers between {a} and {b} included is {countb-counta}")
    return





if __name__ == '__main__':
    import doctest

    doctest.testmod()



#sample answer 自带了一个求素数函数
"""
import sys
from math import sqrt
from itertools import compress

from itertools import chain


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


def f(a, b):
    primes = sieve_of_primes_up_to(b)
    length = len(primes)
    for prime in primes:
        if prime < a:
            length -= 1
        else:
            break
    print(f"The number of prime numbers between {a} and {b} included is {length}")

"""