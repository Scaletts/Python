"""
Author: DuongTruongTho
Date: 09/08/2021
Program: Exersice_05_page_145.py
Problem:
      Assume that data refers to a list of numbers, and result refers to an empty list.
        Write a loop that adds the nonzero values in data to the result list, keeping them
        in their relative positions and excluding the zeros.

Solution:
    7105962
"""
data = [7, 105, 0, 0, 9, 62]

result = ""
for number in data:
   if number != 0:
       result += str(number)
print(result)