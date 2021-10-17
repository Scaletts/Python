"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Project_04_page132.py
Problem:
      Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.py and
        decimalToOctal.py, which convert numbers between the octal and decimal representations of integers.
        These scripts use algorithms that are similar to those of the binaryToDecimal and decimalToBinary
        scripts developed in Section 4-3.


Solution:
    Display result
        Enter a decimal integer: 123
        The octal representation is 173
        The binary representation of 173 is 123
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


def decimalToOctal(decimal):
    if decimal == 0:
        print(0)
    else:
        oString = ''
        while decimal > 0:
            remainder = decimal % 8
            decimal = decimal // 8
            oString = str(remainder) + oString
        return oString


# main

decimal = int(input("Enter a decimal integer: "))
print("The octal representation is", decimalToOctal(decimal))
swapEight(decimalToOctal(decimal))
