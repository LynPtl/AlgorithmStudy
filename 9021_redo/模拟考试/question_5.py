from random import seed, randrange


# x coordinates range between 1 and 10, from left to right.
# y coordinates range between 1 and 10, from bottom to top.
# First four tests illustrate with the 4 corners of the grid,
# mentioned as a comment.
#
# The path stops when following the arrow either gets us out
# of the grid, or back to a point already visited.
#
# Of course you can import and use numpy, but for no benefit I think.
def f(for_seed, x, y):
    '''
    >>> f(0, 1, 10) # Top left corner
    Here is the grid:
       ⬂ ⬂ ⇦ ⬁ ⬃ ⬂ ⬁ ⬃ ⬀ ⇩
       ⇨ ⬁ ⇨ ⇧ ⬁ ⇨ ⬁ ⇧ ⇧ ⬀
       ⬃ ⇧ ⬀ ⬂ ⬀ ⇩ ⬃ ⬃ ⬁ ⇦
       ⇦ ⇧ ⬂ ⇦ ⬃ ⬀ ⇩ ⬀ ⇧ ⇩
       ⇩ ⇩ ⇨ ⬃ ⇧ ⇧ ⬀ ⬃ ⇧ ⬁
       ⬁ ⇧ ⬀ ⇩ ⬁ ⬃ ⇧ ⬂ ⬀ ⇩
       ⬁ ⇨ ⇩ ⇨ ⇦ ⬁ ⬃ ⇧ ⇧ ⇨
       ⇨ ⇦ ⇧ ⬂ ⬁ ⇩ ⇩ ⬂ ⬁ ⬃
       ⬃ ⬀ ⇧ ⬀ ⇧ ⬃ ⬀ ⇩ ⇩ ⇦
       ⬁ ⇧ ⇩ ⬀ ⇨ ⬀ ⬂ ⇦ ⇧ ⇨
    The longest walk from (1, 10) is:
    (1, 10) -- (2, 9)
    >>> f(1, 10, 10) # Top right corner
    Here is the grid:
       ⇨ ⇧ ⬁ ⇧ ⬃ ⬃ ⬃ ⬂ ⇩ ⇧
       ⬃ ⇦ ⬂ ⬂ ⇦ ⬃ ⬁ ⇩ ⇧ ⬀
       ⇦ ⇦ ⇦ ⇦ ⬂ ⇩ ⬂ ⇦ ⇩ ⬃
       ⬃ ⇩ ⬀ ⇩ ⇩ ⬃ ⬁ ⇦ ⬂ ⇧
       ⇨ ⬁ ⇧ ⬀ ⬂ ⇩ ⬁ ⬁ ⬃ ⬂
       ⇦ ⬃ ⇩ ⬂ ⬂ ⇨ ⬀ ⬀ ⇧ ⬃
       ⇧ ⇨ ⬂ ⬀ ⬃ ⇦ ⬃ ⇦ ⬁ ⬂
       ⇨ ⇨ ⇩ ⇦ ⇩ ⇩ ⬂ ⬀ ⬀ ⬃
       ⬁ ⇦ ⬂ ⇨ ⇩ ⬂ ⇦ ⬃ ⬀ ⇩
       ⬂ ⬃ ⬀ ⬂ ⬀ ⇦ ⬀ ⬃ ⇦ ⇩
    The longest walk from (10, 10) is:
    (10, 10)
    >>> f(3, 10, 1) # Bottom right corner
    Here is the grid:
       ⇩ ⇨ ⬀ ⬃ ⇧ ⇦ ⬃ ⬁ ⇩ ⇩
       ⬃ ⬃ ⬂ ⇨ ⇩ ⇨ ⬂ ⇦ ⇧ ⇨
       ⇦ ⬁ ⇦ ⬁ ⬃ ⬂ ⬂ ⬂ ⬃ ⇨
       ⬀ ⇧ ⇦ ⇨ ⬃ ⇩ ⬁ ⬂ ⬁ ⬂
       ⬂ ⬀ ⬂ ⇩ ⬀ ⇦ ⬁ ⇨ ⬀ ⇧
       ⇩ ⬁ ⬁ ⇧ ⇧ ⬃ ⬃ ⇧ ⬀ ⇧
       ⬂ ⇨ ⇦ ⬁ ⬂ ⬂ ⇧ ⇦ ⇦ ⬂
       ⬀ ⬁ ⇩ ⇦ ⬁ ⇦ ⇧ ⇧ ⇦ ⇩
       ⬂ ⬁ ⬁ ⇨ ⇦ ⬀ ⬀ ⬀ ⇨ ⬂
       ⬂ ⬃ ⬂ ⇧ ⬁ ⬂ ⇩ ⬁ ⬂ ⬁
    The longest walk from (10, 1) is:
    (10, 1) -- (9, 2) -- (10, 2)
    >>> f(6, 1, 1) # Bottom left corner
    Here is the grid:
       ⇧ ⬃ ⬁ ⇦ ⇦ ⇨ ⬃ ⬀ ⬀ ⇦
       ⬁ ⬃ ⇩ ⬂ ⇧ ⇩ ⬁ ⇧ ⬂ ⬀
       ⇧ ⬀ ⬂ ⬁ ⬃ ⇧ ⇩ ⬁ ⇧ ⇦
       ⇩ ⬀ ⬃ ⇩ ⇦ ⬀ ⇩ ⬂ ⬁ ⬀
       ⇧ ⇧ ⇩ ⇧ ⬁ ⬁ ⇩ ⬂ ⬃ ⇩
       ⇨ ⇩ ⇦ ⇩ ⇨ ⇦ ⬀ ⬁ ⬀ ⬂
       ⬂ ⬁ ⇨ ⬃ ⇦ ⇨ ⬂ ⬂ ⇧ ⬃
       ⇩ ⇧ ⬃ ⬃ ⬂ ⇧ ⬂ ⬃ ⬁ ⬂
       ⇧ ⇩ ⬁ ⬃ ⬃ ⇨ ⇦ ⇦ ⇧ ⬁
       ⬀ ⇩ ⬁ ⬃ ⬀ ⬁ ⬂ ⬂ ⬃ ⬁
    The longest walk from (1, 1) is:
    (1, 1) -- (2, 2) -- (2, 1)
    >>> f(7, 5, 3)
    Here is the grid:
       ⬀ ⇨ ⬂ ⇦ ⇧ ⇧ ⬀ ⇦ ⇩ ⇦
       ⇧ ⬂ ⬂ ⇧ ⇩ ⇧ ⬂ ⇦ ⇧ ⇩
       ⇦ ⬂ ⇦ ⇩ ⇦ ⇨ ⬁ ⬂ ⇨ ⇧
       ⬁ ⇨ ⇧ ⇩ ⬀ ⇧ ⇧ ⇦ ⇩ ⬃
       ⬂ ⬀ ⬃ ⬃ ⬀ ⬁ ⇩ ⇨ ⇩ ⇧
       ⬁ ⬃ ⬀ ⬃ ⬁ ⇧ ⇧ ⬂ ⇨ ⬀
       ⇨ ⬃ ⬂ ⇦ ⇧ ⬀ ⬀ ⬀ ⬃ ⬃
       ⇧ ⇧ ⬁ ⬃ ⇧ ⇦ ⬁ ⬃ ⬁ ⬂
       ⬀ ⇦ ⬃ ⬀ ⇨ ⇧ ⬃ ⇦ ⇩ ⬁
       ⇨ ⇩ ⬂ ⬂ ⬃ ⇧ ⇨ ⬃ ⬂ ⬁
    The longest walk from (5, 3) is:
    (5, 3) -- (5, 4) -- (5, 5) -- (4, 6) -- (3, 5)
    >>> f(7, 7, 4)
    Here is the grid:
       ⬀ ⇨ ⬂ ⇦ ⇧ ⇧ ⬀ ⇦ ⇩ ⇦
       ⇧ ⬂ ⬂ ⇧ ⇩ ⇧ ⬂ ⇦ ⇧ ⇩
       ⇦ ⬂ ⇦ ⇩ ⇦ ⇨ ⬁ ⬂ ⇨ ⇧
       ⬁ ⇨ ⇧ ⇩ ⬀ ⇧ ⇧ ⇦ ⇩ ⬃
       ⬂ ⬀ ⬃ ⬃ ⬀ ⬁ ⇩ ⇨ ⇩ ⇧
       ⬁ ⬃ ⬀ ⬃ ⬁ ⇧ ⇧ ⬂ ⇨ ⬀
       ⇨ ⬃ ⬂ ⇦ ⇧ ⬀ ⬀ ⬀ ⬃ ⬃
       ⇧ ⇧ ⬁ ⬃ ⇧ ⇦ ⬁ ⬃ ⬁ ⬂
       ⬀ ⇦ ⬃ ⬀ ⇨ ⇧ ⬃ ⇦ ⇩ ⬁
       ⇨ ⇩ ⬂ ⬂ ⬃ ⇧ ⇨ ⬃ ⬂ ⬁
    The longest walk from (7, 4) is:
    (7, 4) -- (8, 5) -- (9, 4) -- (8, 3) -- (7, 2) -- (6, 1) -- (6, 2) -- \
(6, 3) -- (5, 3) -- (5, 4) -- (5, 5) -- (4, 6) -- (3, 5)
    '''
    arrows = {'W': '\u21e6', 'N': '\u21e7', 'E': '\u21e8', 'S': '\u21e9',
              'NW': '\u2b01', 'NE': '\u2b00', 'SE': '\u2b02', 'SW': '\u2b03'
              }
    directions = list(arrows)
    seed(for_seed)
    grid = [[arrows[directions[randrange(8)]] for _ in range(10)]
            for _ in range(10)
            ]
    print('Here is the grid:')
    for row in grid:
        print('  ', *row)

    arrows = {value: key for key, value in arrows.items()}
    # INSERT YOUR CODE HERE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
