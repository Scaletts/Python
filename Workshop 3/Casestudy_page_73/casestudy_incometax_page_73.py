"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: casestudy_imcometax_page_73.py
Problem:
    Case stuDy: An Investment Report
    It has been said that compound interest is the eighth wonder of the world. Our next
    case study, which computes an investment report, shows why.
    request
    Write a program that computes an investment report.
    analysis
    The inputs to this program are the following:
    • An initial amount to be invested (a floating-point number)
    • A period of years (an integer)
    • An interest rate (a percentage expressed as an integer)
    The program uses a simplified form of compound interest, in which the interest is
    computed once each year and added to the total amount invested. The output of
    the program is a report in tabular form that shows, for each year in the term of the
    investment, the year number, the initial balance in the account for that year, the interest earned for that year, and the ending balance for that year. The columns of the
    table are suitably labeled with a header in the first row. Following the output of the
    table, the program prints the total amount of the investment balance and the total
    amount of interest earned for the period. The proposed user interface is shown in
    Figure 3-1.
Solution:
    ....
"""
# Accept the inputs
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))
# Convert the rate to a decimal number
rate = rate / 100
# Initialize the accumulator for the interest
totalInterest = 0.0
# Display the header for the table
print("%4s%18s%10s%16s" % \
    ("Year", "Starting balance","Interest", "Ending balance"))
# Compute and display the results for each year
for year in range(1, years + 1):
 interest= startBalance * rate
endBalance = startBalance + interest
print("%4d%18.2f%10.2f%16.2f" % \
(year, startBalance, interest, endBalance))
startBalance = endBalance
totalInterest += interest
# Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)

# Enter the number of years: 5
# Enter the rate as a %: 5
# Year  Starting balance  Interest  Ending balance
#    5           1000.00     50.00         1050.00
# Ending balance: $1050.00
# Total interest earned: $50.00