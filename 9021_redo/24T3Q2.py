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

if __name__ == "__main__":
    import doctest

    doctest.testmod()