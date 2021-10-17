"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Project_06_page133.py
Problem:
      Use the strategy of the decimal to binary conversion and the bit shift left operation defined in Project 5
        to code a new encryption algorithm. The algorithm should add 1 to each character’s numeric ASCII value,
        convert it to a bit string, and shift the bits of this string one place to the left. A single-space
        character in the encrypted string separates the resulting bit strings.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result
        Enter a message: tho
        1101011 1010011 1100001
"""

Text = input("Enter a message: ")

code = ''

for ch in Text:
    ordValue = ord(ch) + 1

    bString = ''
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue = ordValue // 2
        bString = str(remainder) + bString

    if len(bString) > 1:
        bString = bString[1:] + bString[0]

    code += bString + " "

print(code)
