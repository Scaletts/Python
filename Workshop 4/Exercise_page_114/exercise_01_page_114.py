"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_01_page_114.py
Problem:
      Translate each of the following numbers to decimal numbers:
        a.  11001(2)
        b.  100000(2)
        c.  11111(2)

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        a.  25
        b.  32
        c.  31

"""
bitString = ['11001', '100000', '11111']

for text in bitString:
    decimal = 0
    exponent = len(text) - 1
    for digit in text:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent = exponent - 1
    print("The integer value of bit string '" + text + "' is:", decimal)

