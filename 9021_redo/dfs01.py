from random import seed, randrange
def area(for_seed, sparsity, i, j):
    '''
    You can assume that i and j are both between 0 and 9 included.
    i is the row number (indexed from top to bottom),
    j is the column number (indexed from left to right)
    of the displayed grid.
    
    >>> area(0, 1, 5, 5)
    The grid is:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    The area of the largest empty region of the grid
    containing the point (5, 5) is: 0
    >>> area(0, 1000, 5, 5)
    The grid is:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    The area of the largest empty region of the grid
    containing the point (5, 5) is: 100
    >>> area(0, 3, 6, 2)
    The grid is:
    0 0 1 0 0 0 0 0 0 0
    0 1 0 1 0 1 1 0 0 0
    0 0 1 0 1 0 1 0 0 0
    0 1 0 0 0 0 0 1 0 0
    0 0 0 1 0 1 1 0 0 0
    0 0 1 0 0 0 1 0 0 0
    1 1 0 1 1 1 0 0 1 1
    0 0 0 1 0 0 0 0 1 0
    0 0 1 0 0 0 0 0 1 0
    0 0 0 1 0 1 1 1 1 0
    The area of the largest empty region of the grid
    containing the point (6, 2) is: 9
    >>> area(0, 2, 9, 5)
    The grid is:
    0 0 1 0 0 0 0 0 0 1
    1 0 1 1 0 1 0 1 1 0
    0 1 0 0 0 1 0 0 0 1
    1 1 0 1 0 0 1 0 1 1
    1 1 1 0 1 1 0 0 1 0
    0 1 0 1 0 0 1 0 0 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 0 0 1 1 0 0 0
    0 0 1 0 1 0 0 1 1 1
    0 1 1 0 1 0 0 1 1 1
    The area of the largest empty region of the grid
    containing the point (9, 5) is: 4
    >>> area(0, 2, 2, 7)
    The grid is:
    0 0 1 0 0 0 0 0 0 1
    1 0 1 1 0 1 0 1 1 0
    0 1 0 0 0 1 0 0 0 1
    1 1 0 1 0 0 1 0 1 1
    1 1 1 0 1 1 0 0 1 0
    0 1 0 1 0 0 1 0 0 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 0 0 1 1 0 0 0
    0 0 1 0 1 0 0 1 1 1
    0 1 1 0 1 0 0 1 1 1
    The area of the largest empty region of the grid
    containing the point (2, 7) is: 22
    >>> area(0, 4, 2, 7)
    The grid is:
    0 0 1 0 0 0 0 0 0 0
    0 0 0 1 0 0 0 1 1 0
    0 1 0 0 0 0 0 0 0 1
    1 1 0 1 0 0 0 0 1 0
    0 0 0 0 1 1 0 0 1 0
    0 1 0 0 0 0 1 0 0 0
    0 0 0 0 1 0 0 1 1 0
    0 1 1 0 0 0 0 0 0 0
    0 0 1 0 1 0 0 0 0 1
    0 1 0 0 0 0 0 1 1 0
    The area of the largest empty region of the grid
    containing the point (2, 7) is: 73
    '''

    seed(for_seed)
    grid = [[int(randrange(sparsity) == 0) for _ in range(10)]
            for _ in range(10)
            ]
    print('The grid is:')
    for row in grid:
        print(*row)
        
    # print('The area of the largest empty region of the grid')
    # print(f'containing the point ({i}, {j}) is: ', end='')

    # ADD YOUR CODE HERE (A PRINT STATEMENT AT THE END IS NEEDED)
    cur = grid[i][j]
    if cur == 1:
        print('The area of the largest empty region of the grid')
        print(f'containing the point ({i}, {j}) is: 0', end='')
        return
    else:
        visited = set()
        times = dfs(grid,visited,i,j)
        print('The area of the largest empty region of the grid')
        print(f'containing the point ({i}, {j}) is: {times}', end='')
        return

def dfs(grid,visited,i,j):
    if grid[i][j] == 1 or (i,j) in visited:
        return 0
    method = [(0,1),(0,-1),(1,0),(-1,0)]
    times = 1
    visited.add((i,j))
    for x,y in method:
        if 0 <= i + x <= 9 and 0 <= j + y <= 9:
            times += dfs(grid,visited,i+x,j+y)
    return times

#sample answer
"""
    print('The area of the largest empty region of the grid')
    print(f'containing the point ({i}, {j}) is: ', end='')

    # ADD YOUR CODE HERE (A PRINT STATEMENT AT THE END IS NEEDED)
    print(dfs(grid, i, j))


# POSSIBLY DEFINE OTHER FUNCTIONS
def dfs(grid, row, col):
    if 0 <= row < 10 and 0 <= col < 10 and grid[row][col] == 0:
        grid[row][col] = 1
        return 1 + dfs(grid, row, col + 1) + dfs(grid, row + 1, col) + dfs(grid, row, col - 1) + dfs(grid, row - 1, col)

    return 0
"""
# POSSIBLY DEFINE OTHER FUNCTIONS


if __name__ == '__main__':
    import doctest

    doctest.testmod()
