"""
Author: Dương Trường Thọ
Date: 11/07/2021
Program: project_01_page_62-63.py
Problem:
    The tax calculator program of the case study outputs a floating-point number
    that might show more than two digits of precision. Use the round function to
    modify the program to display at most two digits of precision in the output
    number.
    
Solution:
    ....
"""
#The tax calculator program of the case study outputs a floating-point number that might show more than two digits of precision. Use the round function to modify the program to display at most two digits of precision in the output number.
# Initialize the constants
from typing import Match
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
# Display the income tax
print("The income tax is $" + str(incomeTax))
#Enter the gross income: 100
#Enter the number of dependents: 100
#The income tax is $-61980.0


