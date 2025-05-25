# 纯回忆题
import doctest
def f(n):
    """
    >>> f(2224444)
    0
    >>> f(12)
    1
    >>> f(123)
    13
    >>> f(11113333)
    11113333
    >>> f(111122223333)
    11113333
    >>> f(9201012)
    911
    """
    result = "0"
    for num in str(n):
        if int(num) % 2 != 0:
            result += num
    print(int(result))

if __name__ == "__main__":
    doctest.testmod()
