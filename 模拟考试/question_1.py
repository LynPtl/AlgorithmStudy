from itertools import cycle
from itertools import zip_longest
def f(size, characters):
    """
    >>> f(size=4, characters='12345')
          1
        1 2
      1 2 3
    1 2 3 4
      3 4 5
        5 1
          2
    >>> f(size=4, characters='ABCD')
          A
        A B
      A B C
    A B C D
      C D A
        A B
          C
    >>> f(size=5, characters='ABCD')
            A
          A B
        A B C
      A B C D
    A B C D A
      C D A B
        A B C
          C D
            A
    >>> f(size=7, characters='ABCD')
                A
              A B
            A B C
          A B C D
        A B C D A
      A B C D A B
    A B C D A B C
      C D A B C D
        A B C D A
          C D A B
            A B C
              C D
                A
    """
    # Insert your code here
    columns = []
    for col_index in range(size):
      length = 1 + col_index * 2 
      cyc = cycle(characters)
      column = ""
      for _ in range(length):
        column += next(cyc)
      column = " " * (size -col_index - 1) + column
      columns.append(column)
    for line in zip_longest(*columns, fillvalue=" "):
        print((" ".join(line)).rstrip())
if __name__ == "__main__":
    import doctest

    doctest.testmod()
