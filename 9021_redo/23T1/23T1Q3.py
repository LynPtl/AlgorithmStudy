from itertools import cycle
import string
def rhombus(size, shift_right=False):
    '''
    >>> rhombus(1)
    A
    >>> rhombus(1, True)
    A
    >>> rhombus(2)
     BA
    CD
    >>> rhombus(2, True)
    AB
     DC
    >>> rhombus(3)
      CBA
     DEF
    IHG
    >>> rhombus(3, True)
    ABC
     FED
      GHI
    >>> rhombus(4)
       DCBA
      EFGH
     LKJI
    MNOP
    >>> rhombus(4, True)
    ABCD
     HGFE
      IJKL
       PONM
    >>> rhombus(7)
          GFEDCBA
         HIJKLMN
        UTSRQPO
       VWXYZAB
      IHGFEDC
     JKLMNOP
    WVUTSRQ
    >>> rhombus(7, True)
    ABCDEFG
     NMLKJIH
      OPQRSTU
       BAZYXWV
        CDEFGHI
         PONMLKJ
          QRSTUVW
    '''
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    cyc = cycle(string.ascii_uppercase)
    need = ""
    for i in range(size**2):
        need += next(cyc)
    cur = 0
    if shift_right == True:
        for i in range(size):
            space =  " " * i
            if  i % 2 == 0:
                line = space + need[cur: cur + size]
                cur = cur + size
            else:
                line = space + need[cur: cur + size][::-1]
                cur = cur + size
            print(line)
    else:
        for i in range(size):
            space = " " * (size - i- 1)
            if i % 2 == 0:
                line = space + need[cur: cur + size][::-1]
                cur = cur + size
            else:
                line = space + need[cur: cur + size]
                cur = cur + size
            print(line)
    return
    #sample answer
    """
    for row in range(size):
        line = ""
        for col in range(size):
            line += chr( ord('A') + (size * row + col) % 26)

        if shift_right:
            if row % 2 == 0:
                print(row * ' ' + line)
            else:
                print(row * ' ' + line[::-1])
        else:
            if row % 2 == 0:
                print((size - row - 1) * ' ' + line[::-1])
            else:
                print((size - row - 1) * ' ' + line)
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
