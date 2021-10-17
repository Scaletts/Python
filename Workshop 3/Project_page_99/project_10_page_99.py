"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: project_10_page_99.py
Problem:
    The credit plan at TidBit Computer Store specifies a 10% down payment and
    an annual interest rate of 12%. Monthly payments are 5% of the listed purchase
    price, minus the down payment. Write a program that takes the purchase price
    as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain
    the following items:
    • the month number (beginning with 1)
    • the current total balance owed
    • the interest owed for that month
    • the amount of principal owed for that month
    • the payment for that month
    • the balance remaining after payment
    The amount of interest for a month is equal to balance * rate / 12. The amount of
    principal for a month is equal to the monthly payment minus the interest owed.
Solution:
    
    ....
"""
# Total price
price = float(input("Total computer cost:"))
# Price after down payment
remaining_price = (price * 0.9)
# Monthly payment (5 percent of remaining price)
monthly_payment = remaining_price * 0.05
# Interest owed for this month
interest_owed = remaining_price * (.12/12.0)
# Principal for this month
principal = monthly_payment - interest_owed
# Month 
month = 0
# Print stuff
print("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" %(month, price, interest_owed, principal, monthly_payment, remaining_price))
while remaining_price > 0:
    month += 1
    remaining_price -= principal
    interest_owed = remaining_price * (.12/12.0)
    principal = monthly_payment - interest_owed
    print("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" %(month, price, interest_owed, principal, monthly_payment, remaining_price))

# Total computer cost:10
# 0 Months               10.00               0.090                0.36         0.45                   9.00
# 1 Months               10.00               0.086                0.36         0.45                   8.64
# 2 Months               10.00               0.083                0.37         0.45                   8.28
# 3 Months               10.00               0.079                0.37         0.45                   7.91
# 4 Months               10.00               0.075                0.37         0.45                   7.54
# 5 Months               10.00               0.072                0.38         0.45                   7.16
# 6 Months               10.00               0.068                0.38         0.45                   6.79
# 7 Months               10.00               0.064                0.39         0.45                   6.40
# 8 Months               10.00               0.060                0.39         0.45                   6.02
# 9 Months               10.00               0.056                0.39         0.45                   5.63
# 10 Months               10.00               0.052                0.40         0.45                   5.23
# 11 Months               10.00               0.048                0.40         0.45                   4.84
# 12 Months               10.00               0.044                0.41         0.45                   4.43
# 13 Months               10.00               0.040                0.41         0.45                   4.03
# 14 Months               10.00               0.036                0.41         0.45                   3.62
# 15 Months               10.00               0.032                0.42         0.45                   3.21
# 16 Months               10.00               0.028                0.42         0.45                   2.79
# 17 Months               10.00               0.024                0.43         0.45                   2.37
# 18 Months               10.00               0.019                0.43         0.45                   1.94
# 19 Months               10.00               0.015                0.43         0.45                   1.51
# 20 Months               10.00               0.011                0.44         0.45                   1.07
# 21 Months               10.00               0.006                0.44         0.45                   0.63
# 22 Months               10.00               0.002                0.45         0.45                   0.19
# 23 Months               10.00              -0.003                0.45         0.45                  -0.26