from itertools import cycle
def f(size, characters):
    """
    >>> f(size=4, characters='12345')
    1 2 3 4
     5 1 2
      3 4
       5
       1
      2 3
     4 5 1
    2 3 4 5
    >>> f(size=3, characters='-+')
    - + -
     + -
      +
      -
     + -
    + - +
    >>> f(size=7, characters='A#B')
    A # B A # B A
     # B A # B A
      # B A # B
       A # B A
        # B A
         # B
          A
          #
         B A
        # B A
       # B A #
      B A # B A
     # B A # B A
    # B A # B A #
    """
    cyc = cycle(characters)
    #上半部分
    for i in range(size):
        line = []
        space = " " * i
        for times in range(size-i):
            line.append(next(cyc))
        outputline = space + ' '.join(line)
        print(outputline)
    #下半部分
    for i in range(size):
        line = []
        space = " " * (size - i - 1)
        for times in range(i + 1):
            line.append(next(cyc))
        outputline = space + ' '.join(line)
        print(outputline)
    return
    #sample answer
    """
    from itertools import cycle
    iterator = cycle(characters)
    for row in range(size-1, -1, -1):
        line = ""
        for col in range(row + 1):
            line += next(iterator)
        print(" " * (size - row -1) + " ".join(line))

    for row in range(size):
        line = ""
        for col in range(row + 1):
            line += next(iterator)
        print(" " * (size - row - 1) + " ".join(line))
    """
    
    #以下是一个claude写法
    """
    total_rows = 2 * size
    char_index = 0  # 全局字符索引，用于跟踪当前应该使用的字符
    
    for row in range(total_rows):
        if row < size:
            # 上半部分（包括中间行）
            spaces = row
            chars_count = size - row
        else:
            # 下半部分
            spaces = total_rows - 1 - row
            chars_count = row - size + 1
        
        # 生成前导空格
        line = ' ' * spaces
        
        # 生成字符序列
        chars = []
        for i in range(chars_count):
            chars.append(characters[char_index % len(characters)])
            char_index += 1
        
        # 用空格连接字符并添加到行中
        line += ' '.join(chars)
        
        print(line)
    """

if __name__ == "__main__":
    import doctest

    doctest.testmod()