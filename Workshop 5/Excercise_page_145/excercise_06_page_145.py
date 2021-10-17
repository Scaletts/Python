"""
Author: DuongTruongTho
Date: 09/08/2021
Program: Exersice_06_page_145.py
Problem:
      Write a loop that replaces each number in a list named data with its absolute value.

Solution:
        The original list is : [5, -6, 7, -8, -10]
        Absolute value list : [5, 6, 7, 8, 10]
"""
# initialize list
test_list = [5, -6, 7, -8, -10]
  
# printing original list
print("The original list is : " + str(test_list))
  
# Absolute value of list elements
# using abs() + list comprehension
res =  [abs(ele) for ele in test_list]
  
# printing result
print("Absolute value list : " + str(res))