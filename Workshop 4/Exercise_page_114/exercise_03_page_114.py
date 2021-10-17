"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_03_page_114.py
Problem:
      Translate each of the following numbers to binary numbers:
        a.  47(8)
        b.  127(8)
        c.  64(8)

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        a.  100111
        b.  1010111
        c.  110100

"""

def swapTen(decimal):
    if decimal == 0:
        print(0)
    else:
        bitString = ''
        while decimal > 0:
            remainder = decimal % 2
            decimal = decimal // 2
            bitString = str(remainder) + bitString

    return bitString


def swapEight(decimal):
    a = decimal
    length = len(decimal)
    decimal = int(decimal)
    total = 0
    for i in range(0, length):
        index = decimal % 10
        total += (index * pow(8, i))
        decimal //= 10

    print("The binary representation of", str(a), "is", swapTen(total))


# main
element = ['47', '127', '64']
swap = []

for decimal in element:
    swap.append(swapEight(decimal))

