"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_02_page_85.py
Problem:
    Assume that x refers to a number. Write a code segment that prints the number’s
    absolute value without using Python’s abs function.
Solution:
    import math
    # Some random values
    valueA = -4
    valueB = -56
    valueC = 26
    valueD = -2.992474203
    # Get the floating-point absolute value from each
    fabs_A = math.fabs(valueA)
    fabs_B = math.fabs(valueB)
    fabs_C = math.fabs(valueC)
    fabs_D = math.fabs(valueD)
    # Output the results
    print("Absolute floating-point values with `fabs()`:")
    print("|", valueA, "| = ", fabs_A, sep="")
    print("|", valueB, "| = ", fabs_B, sep="")
    print("|", valueC, "| = ", fabs_C, sep="")
    print("|", valueD, "| = ", fabs_D, sep="")
    ....
"""
import math
# Some random values
valueA = -4
valueB = -56
valueC = 26
valueD = -2.992474203
# Get the floating-point absolute value from each
fabs_A = math.fabs(valueA)
fabs_B = math.fabs(valueB)
fabs_C = math.fabs(valueC)
fabs_D = math.fabs(valueD)
# Output the results
print("Absolute floating-point values with `fabs()`:")
print("|", valueA, "| = ", fabs_A, sep="")
print("|", valueB, "| = ", fabs_B, sep="")
print("|", valueC, "| = ", fabs_C, sep="")
print("|", valueD, "| = ", fabs_D, sep="")

# Absolute floating-point values with `fabs()`:
# |-4| = 4.0
# |-56| = 56.0
# |26| = 26.0
# |-2.992474203| = 2.992474203