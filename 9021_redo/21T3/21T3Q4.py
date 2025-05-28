# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 4

'''
No point to hard code for small values of n, will be tested
only for large enough values...
'''

def pascal_triangle_line(n):
    '''
    Recall: it is the list of binomial coefficients that give the
    number of ways of choosing k objects out of n - 1 for 0 <= k < n.

    >>> pascal_triangle_line(1)
    [1]
    >>> pascal_triangle_line(2)
    [1, 1]
    >>> pascal_triangle_line(3)
    [1, 2, 1]
    >>> pascal_triangle_line(4)
    [1, 3, 3, 1]
    >>> pascal_triangle_line(5)
    [1, 4, 6, 4, 1]
    >>> pascal_triangle_line(6)
    [1, 5, 10, 10, 5, 1]
    >>> pascal_triangle_line(7)
    [1, 6, 15, 20, 15, 6, 1]
    >>> pascal_triangle_line(8)
    [1, 7, 21, 35, 35, 21, 7, 1]
    '''
    
    # return
    # REPLACE return WITH YOUR CODE
    #sample answer
    from math import comb
    return [comb(n - 1, i) for i in range(n)]

    # 非包算法
    """
    if n == 1:
    return [1]
    
    # 构建完整的杨辉三角，直到第n行
    triangle = [[1]]  # 第一行
    
    for row_num in range(2, n + 1):
        prev_row = triangle[-1]  # 上一行
        new_row = [1]  # 新行的第一个元素
        
        # 计算新行的中间元素
        for i in range(1, row_num - 1):
            new_row.append(prev_row[i - 1] + prev_row[i])
        
        new_row.append(1)  # 新行的最后一个元素
        triangle.append(new_row)
    
    return triangle[-1]  # 返回最后一行
    """
if __name__ == '__main__':
    import doctest
    doctest.testmod()

