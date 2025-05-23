import sys

def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that:
    - i + j is even;
    - when read from left to right, the digits in i are strictly increasing
    - when read from left to right, the digits in j are strictly decreasing
    - when read from left to right, the digits in the average of i and j are
      either strictly increasing or strictly decreasing

    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    
    >>> f(10, 20)
    12 and 20 with 16 as average
    14 and 20 with 17 as average
    16 and 20 with 18 as average
    18 and 20 with 19 as average
    >>> f(30, 50)
    34 and 40 with 37 as average
    34 and 42 with 38 as average
    34 and 50 with 42 as average
    35 and 41 with 38 as average
    35 and 43 with 39 as average
    36 and 40 with 38 as average
    36 and 42 with 39 as average
    36 and 50 with 43 as average
    37 and 41 with 39 as average
    37 and 43 with 40 as average
    38 and 40 with 39 as average
    38 and 42 with 40 as average
    39 and 41 with 40 as average
    39 and 43 with 41 as average
    46 and 50 with 48 as average
    48 and 50 with 49 as average
    >>> f(400, 700)
    456 and 630 with 543 as average
    457 and 521 with 489 as average
    458 and 520 with 489 as average
    459 and 621 with 540 as average
    468 and 510 with 489 as average
    478 and 542 with 510 as average
    479 and 541 with 510 as average
    489 and 531 with 510 as average
    567 and 653 with 610 as average
    568 and 610 with 589 as average
    568 and 652 with 610 as average
    569 and 651 with 610 as average
    578 and 642 with 610 as average
    579 and 641 with 610 as average
    589 and 631 with 610 as average
    589 and 651 with 620 as average
    589 and 653 with 621 as average
    '''
    for i in range(a,b+1):
        stri = str(i)
        is_increase = True
        for d in range(len(stri)-1):
            if stri[d] >= stri[d+1]:
                is_increase = False
                break
        if is_increase == False:
            continue
        for j in range(i+1,b+1):
            if (i+j)%2 != 0:
                continue
            strj = str(j)
            is_decrease = True
            for d in range(len(strj)-1):
                if strj[d] <= strj[d+1]:
                    is_decrease = False
                    break
            if is_decrease == False:
                continue
            avg = (i+j)//2
            stravg = str(avg)
            av_is_increase = True
            av_is_decrease = True
            for d in range(len(stravg)-1):
                if stravg[d] <= stravg[d+1]:
                    av_is_decrease = False
                if stravg[d] >= stravg[d+1]:
                    av_is_increase = False
            if av_is_increase or av_is_decrease:
                print(f"{i} and {j} with {int((i+j)//2)} as average")


if __name__ == '__main__':
    import doctest
    doctest.testmod()




#以下是sample answer
"""
import sys


def check_increasing(n):
    m = str(n)

    first = m[0]
    for second in m[1:]:
        if int(first) >= int(second):
            return False
        first = second

    return True


def check_decreasing(n):
    m = str(n)

    first = m[0]
    for second in m[1:]:
        if int(first) <= int(second):
            return False
        first = second

    return True


def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that:
    - i + j is even;
    - when read from left to right, the digits in i are strictly increasing
    - when read from left to right, the digits in j are strictly decreasing
    - when read from left to right, the digits in the average of i and j are
      either strictly increasing or strictly decreasing

    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    
    >>> f(10, 20)
    12 and 20 with 16 as average
    14 and 20 with 17 as average
    16 and 20 with 18 as average
    18 and 20 with 19 as average
    >>> f(30, 50)
    34 and 40 with 37 as average
    34 and 42 with 38 as average
    34 and 50 with 42 as average
    35 and 41 with 38 as average
    35 and 43 with 39 as average
    36 and 40 with 38 as average
    36 and 42 with 39 as average
    36 and 50 with 43 as average
    37 and 41 with 39 as average
    37 and 43 with 40 as average
    38 and 40 with 39 as average
    38 and 42 with 40 as average
    39 and 41 with 40 as average
    39 and 43 with 41 as average
    46 and 50 with 48 as average
    48 and 50 with 49 as average
    >>> f(400, 700)
    456 and 630 with 543 as average
    457 and 521 with 489 as average
    458 and 520 with 489 as average
    459 and 621 with 540 as average
    468 and 510 with 489 as average
    478 and 542 with 510 as average
    479 and 541 with 510 as average
    489 and 531 with 510 as average
    567 and 653 with 610 as average
    568 and 610 with 589 as average
    568 and 652 with 610 as average
    569 and 651 with 610 as average
    578 and 642 with 610 as average
    579 and 641 with 610 as average
    589 and 631 with 610 as average
    589 and 651 with 620 as average
    589 and 653 with 621 as average
    '''
    for i in range(a, b + 1):
        for j in range(i + 1, b + 1):
            if (i + j) % 2 == 0:
                if check_increasing(i) and check_decreasing(j):
                    even = (i + j) // 2
                    if check_increasing(even) or check_decreasing(even):
                        print(f"{i} and {j} with {even} as average")


if __name__ == '__main__':
    import doctest

    doctest.testmod()
"""