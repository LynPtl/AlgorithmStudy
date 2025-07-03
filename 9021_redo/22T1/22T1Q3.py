# Will be tested only with strictly positive integers for
# total_nb_of_letters and height.
#
# <BLANKLINE> is not output by the program, but
# doctest's way to refer to an empty line.
# For instance,
#    A
#    B
#    C
#    <BLANKLINE>
#    <BLANKLINE>
# means that 5 lines are output: first a line with A,
# then a line with B, then a line with C,
# and then 2 empty lines.
#
# Note that no line has any trailing space.

def f(total_nb_of_letters, height):
    '''
    >>> f(4, 1)
    ABCD
    >>> f(3, 5)
    A
    B
    C
    <BLANKLINE>
    <BLANKLINE>
    >>> f(4, 2)
    AD
    BC
    >>> f(5, 2)
    ADE
    BC
    >>> f(6, 2)
    ADE
    BCF
    >>> f(7, 2)
    ADE
    BCFG
    >>> f(8, 2)
    ADEH
    BCFG
    >>> f(9, 2)
    ADEHI
    BCFG
    >>> f(17,5)
    AJK
    BIL
    CHM
    DGNQ
    EFOP
    >>> f(100, 6)
    ALMXYJKVWHITUFGRS
    BKNWZILUXGJSVEHQT
    CJOVAHMTYFKRWDIPU
    DIPUBGNSZELQXCJOV
    EHQTCFORADMPYBKN
    FGRSDEPQBCNOZALM
    '''
    # INSERT YOUR CODE HERE
    import string
    from itertools import cycle , zip_longest
    iterator = cycle(string.ascii_uppercase)
    letters = ""
    for num in range(total_nb_of_letters):
        letters += next(iterator)
    lines = []
    for i in range(0,total_nb_of_letters,height):
        line_no = i // height
        each_line = letters[i:i+height]
        if line_no % 2 == 0:
            # each_line = each_line.ljust(height)
            each_line = f"{each_line:<{height}}"
        else:
            each_line = each_line[::-1].rjust(height)
        lines.append(each_line)
    for line in zip_longest(*lines,fillvalue=" "):
        print("".join(line).rstrip())

if __name__ == '__main__':
    import doctest

    doctest.testmod()
