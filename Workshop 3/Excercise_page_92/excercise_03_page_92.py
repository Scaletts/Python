"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_03_page_92.py
Problem:
    The log 2 of a given number N is given by M in the equation N 5 2M. Using integer
    arithmetic, the value of M is approximately equal to the number of times N can be
    evenly divided by 2 until it becomes 0. Write a loop that computes this approximation of the log 2 of a given number N. You can check your code by importing the
    math.log function and evaluating the expression round(math.log(N, 2)) (note
    that the math.log function returns a floating-point value).
Solution:
    import math
    x=int(input("Enter your number:"))
    log2 = math.log(x, 2.0)
    log2 = math.log2(x)
    print(log2)
    ....
"""
# import math
# x=int(input("Enter your number:"))
# log2 = math.log(x, 2.0)
# log2 = math.log2(x)
# print(log2)

# Enter your number:5
# 2.321928094887362


