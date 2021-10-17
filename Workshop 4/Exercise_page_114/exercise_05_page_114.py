"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_05_page_114.py
Problem:
      Translate each of the following numbers to decimal numbers:
        a.  47(16)
        b.  127(16)
        c.  AA(16)

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        a.  71
        b.  295
        c.  170

"""

def swapSixteen(decimal):
    LETTER = '0123456789ABCDEF'
    a = decimal
    length = len(decimal) - 1
    total = 0

    for index in decimal:
        if index in LETTER:
            index = LETTER.find(index)
            total += (int(index) * pow(16, length))
            length -= 1

    print("The binary representation of", str(a), "is", total)


# main
element = ['47', '127', 'AA']
for decimal in element:
    swapSixteen(decimal)

