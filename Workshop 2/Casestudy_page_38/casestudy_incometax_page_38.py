"""
Author: Dương Trường Thọ
Date: 11/07/2021
Program: casestudy_imcometax_page_38.py
Problem:
    CaSe StuDy: Income Tax Calculator
    Most of the chapters in this book include a case study that illustrates the software
    development process. This approach may seem overly elaborate for small programs,
    but it scales up well when programs become larger. The first case study develops a
    program that calculates income tax.
    Each year, nearly everyone with an income faces the unpleasant task of computing
    his or her income tax return. If only it could be done as easily as suggested in this
    case study! We start with the customer request phase.
    request
    The customer requests a program that computes a person’s income tax.
    analysis
    Analysis often requires the programmer to learn some things about the problem
    domain, in this case, the relevant tax law. For the sake of simplicity, let’s assume the
    following tax laws:
    • All taxpayers are charged a flat tax rate of 20%.
    • All taxpayers are allowed a $10,000 standard deduction.
    • For each dependent, a taxpayer is allowed an additional $3,000 deduction.
    • Gross income must be entered to the nearest penny.
    • The income tax is expressed as a decimal number.
    Another part of analysis determines what information the user will have to provide.
    In this case, the user inputs are gross income and number of dependents. The
    program calculates the income tax based on the inputs and the tax law and then
    displays the income tax. Figure 2-4 shows the proposed terminal-based interface.
    Characters in italics indicate user inputs. The program prints the rest. The inclusion
    of an interface at this point is a good idea because it allows the customer and the
    programmer to discuss the intended program’s behavior in a context understandable to both.
Solution:
    ....
"""
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