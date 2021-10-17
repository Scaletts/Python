"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_03_page_73.py
Problem:
    Write a format operation that builds a string for the float variable amount that has
    exactly two digits of precision and a field width of zero.
Solution:
    print ("Your salary is $ " +  ("%0.2f" %amount))
    ....
"""
amount=24.325
print ("Your salary is $ " +  ("%0.2f" %amount))
#Your salary is $ 24.32