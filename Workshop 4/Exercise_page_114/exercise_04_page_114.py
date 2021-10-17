"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_04_page_114.py
Problem:
      Translate each of the following numbers to decimal numbers:
        a.  47(8)
        b.  127(8)
        c.  64(8)

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        a.  39
        b.  87
        c.  52

"""

def swapEight(decimal):
    a = decimal
    length = len(decimal)
    decimal = int(decimal)
    total = 0
    for i in range(0, length):
        index = decimal % 10
        total += (index * pow(8, i))
        decimal //= 10

    print("The binary representation of", str(a), "is", total)


# main
element = ['47', '127', '64']
for decimal in element:
    swapEight(decimal)
