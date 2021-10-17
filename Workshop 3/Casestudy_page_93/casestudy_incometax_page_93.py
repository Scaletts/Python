"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: casestudy_imcometax_page_93.py
Problem:
    Case stuDy: Approximating Square Roots
    Users of pocket calculators or Python’s math module do not have to think about how
    to compute square roots, but the people who built those calculators or wrote the
    code for that module certainly did. In this case study, we open the hood and see how
    this might be done.
    request
    Write a program that computes square roots.
    (continues)
    Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
    Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.
    Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. WCN 02-200-20393
    analysis
    The input to this program is a positive floating-point number or an integer. The output is a floating-point number representing the square root of the input number. For
    purposes of comparison, we also output Python’s estimate of the square root using math.sqrt. 
Solution:
    ....
"""
import math
# Receive the input number from the user
x = float(input("Enter a positive number: "))
# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0
# Perform the successive approximations
while True:
 estimate = (estimate + x / estimate) / 2
 difference = abs(x - estimate ** 2)
 if difference <= tolerance:
   break
# Output the result
print("The program's estimate:", estimate)
print("Python's estimate: ", math.sqrt(x))

# Enter a positive number: 3
# The program's estimate: 1.7320508100147274
# Python's estimate:  1.7320508075688772