"""
Author: DuongTruongTho
Date: 09/08/2021
Program: Exersice_04_page_145.py
Problem:
      Write a loop that accumulates the sum of the numbers in a list named data

Solution:
        20
"""
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))