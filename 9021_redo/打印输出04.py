# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.

from itertools import cycle
import string
def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    cyc = cycle(string.ascii_lowercase)
    for i in range(height):
        line = ""
        for j in range(width):
            line += next(cyc)
        if i % 2 != 0:
            line = line[::-1]
        print(line)
    return
if __name__ == '__main__':
    import doctest
    doctest.testmod()
