# Hint: To avoid arithmetic computations, zip columns.
#
# count, from itertools, can be used to push arithmetic laziness
# even further...
#
# You can assume that the function is called with height
# a strictly positive integer.


from itertools import count
from itertools import cycle,zip_longest
import string
def triangle(height):
    '''
    >>> triangle(1)
    A
    >>> triangle(2)
    A
    B
    >>> triangle(3)
    A
    B D
    C
    >>> triangle(4)
    A
    B E
    C F
    D
    >>> triangle(5)
    A
    B F
    C G I
    D H
    E
    >>> triangle(6)
    A
    B G
    C H K
    D I L
    E J
    F
    >>> triangle(7)
    A
    B H
    C I M
    D J N P
    E K O
    F L
    G
    >>> triangle(8)
    A
    B I
    C J O
    D K P S
    E L Q T
    F M R
    G N
    H
    >>> triangle(9)
    A
    B J
    C K Q
    D L R V
    E M S W Y
    F N T X
    G O U
    H P
    I
    >>> triangle(10)
    A
    B K
    C L S
    D M T Y
    E N U Z C
    F O V A D
    G P W B
    H Q X
    I R
    J
    >>> triangle(11)
    A
    B L
    C M U
    D N V B
    E O W C G
    F P X D H J
    G Q Y E I
    H R Z F
    I S A
    J T
    K
    '''
    pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
    cyc = cycle(string.ascii_uppercase)
    row = 0
    result = []
    while height > 0 :
        line = ""
        space = " " * row
        line += space
        for i in range(height):
            line += next(cyc)
        height = height - 2
        row += 1
        result.append(line)
    for i in zip_longest(*result , fillvalue=" "):
        print(" ".join(i).strip())

    #sample answer
    """
    lines = []
    start = 0
    while height > 0:
        line = ""
        for i in range(height):
            line += chr(ord('A') + start % 26)
            start += 1
            lines.append(len(lines * " " + line))
            height = height - 2

    from itertools import zip_longest
    for line in zip_longest(*lines,fillvalue=" "):
        print(" ".join(line).strip())
    """
if __name__ == '__main__':
    import doctest

    doctest.testmod()
