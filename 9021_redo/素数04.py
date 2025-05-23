"""
Will be tested with n at least equal to 2, and "not too large".
"""

from math import sqrt
from collections import defaultdict


def f(n):
    """
    >>> f(2)
    The decomposition of 2 into prime factors reads:
       2 = 2
    >>> f(3)
    The decomposition of 3 into prime factors reads:
       3 = 3
    >>> f(4)
    The decomposition of 4 into prime factors reads:
       4 = 2^2
    >>> f(5)
    The decomposition of 5 into prime factors reads:
       5 = 5
    >>> f(6)
    The decomposition of 6 into prime factors reads:
       6 = 2 x 3
    >>> f(8)
    The decomposition of 8 into prime factors reads:
       8 = 2^3
    >>> f(10)
    The decomposition of 10 into prime factors reads:
       10 = 2 x 5
    >>> f(15)
    The decomposition of 15 into prime factors reads:
       15 = 3 x 5
    >>> f(100)
    The decomposition of 100 into prime factors reads:
       100 = 2^2 x 5^2
    >>> f(5432)
    The decomposition of 5432 into prime factors reads:
       5432 = 2^3 x 7 x 97
    >>> f(45103)
    The decomposition of 45103 into prime factors reads:
       45103 = 23 x 37 x 53
    >>> f(45100)
    The decomposition of 45100 into prime factors reads:
       45100 = 2^2 x 5^2 x 11 x 41
    """
    # Insert your code here
    from collections import defaultdict

    result = defaultdict(int)
    m = n
    for num in range(2, n + 1):
        if m == 1:
            break
        while m % num == 0:
            result[num] += 1
            m = m // num
    # 这里并不需要把素数全都列举出来，用简单的遍历+除法就一定是素数
    print(f"The decomposition of {n} into prime factors reads:")
    if result:
        factors = []
        for k in sorted(result.keys()):
            v = result[k]
            if v == 1:
                factors.append(str(k))
            else:
                factors.append(f"{k}^{v}")
        print(f"   {n} = {' x '.join(factors)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
