from math import sqrt

    
def f(n, d):
    '''
    >>> f(2, 1)
    1 is not a proper factor of 2.
    >>> f(2, 2)
    2 is not a proper factor of 2.
    >>> f(16, 2)
    2 is a proper factor of 16 of mutiplicity 4.
    >>> f(100, 20)
    20 is a proper factor of 100 of mutiplicity 1.
    >>> f(8 ** 7 * 3 ** 5 * 11 ** 2, 8)
    8 is a proper factor of 61662560256 of mutiplicity 7.
    >>> f(3 ** 3 * 11 * 13 ** 2 * 40 ** 6, 8)
    8 is a proper factor of 205590528000000 of mutiplicity 6.
    '''
    flag = True
    if d == 1 or d == n:
        flag = False
        return output(flag,n,d)
    else:
        if (n % d != 0):
            flag = False
            return output(flag,n,d)
        else:
            times = 0
            n_cp = n
            while n_cp % d == 0:
                times += 1
                n_cp = n_cp//d
    return output(flag,n,d,times)

def output(flag,n,d,times=0):
    if flag == False:
        print(f"{d} is not a proper factor of {n}.")
    else:
        print(f"{d} is a proper factor of {n} of mutiplicity {times}.")


if __name__ == '__main__':
    import doctest

    doctest.testmod()


#sample answer
'''
    if d == 1 or n == d or n % d != 0:
        print(f"{d} is not a proper factor of {n}.")
        return

    mutiplicity = 0
    m = n
    while m % d == 0:
        m = m // d
        mutiplicity += 1
    print(f"{d} is a proper factor of {n} of mutiplicity {mutiplicity}.")
'''