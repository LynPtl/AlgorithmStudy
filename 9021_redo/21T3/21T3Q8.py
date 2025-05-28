# Final Exam Question 8

def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    Conjunctions of inputs will be tested, so hard coding will not help.
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''

    # return
    # REPLACE return WITH YOUR CODE
    import numpy as np
    grid = np.array(square)
    result = [np.sum(grid[i]) for i in range(len(grid))]
    result.extend([np.sum(grid[:,i]) for i in range(len(grid[0]))])
    result.extend([np.sum(grid.diagonal()),np.sum(np.fliplr(grid).diagonal())])
    if len(result) == len(set(result)):
        return True
    return False
# POSSIBLY DEFINE OTHER FUNCTIONS


if __name__ == '__main__':
    import doctest

    doctest.testmod()
