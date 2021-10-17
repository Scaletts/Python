"""
Author: Dương Trường Thọ
Date: 11/07/2021
Program: project_10_page_62-63.py
Problem:
    
    An employee’s total weekly pay equals the hourly wage multiplied by the total
    number of regular hours plus any overtime pay. Overtime pay equals the total
    overtime hours multiplied by 1.5 times the hourly wage. Write a program that
    takes as inputs the hourly wage, total regular hours, and total overtime hours and
    displays an employee’s total weekly pay.
Solution:
    ....
"""

# An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. Overtime pay equals the total
   #overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and
   #displays an employee’s total weekly pay.
hourWage= float(input ("What is your hourly wage?: "))
regularHours= float(input ("How many regular hours did you work this week?: "))
overtimeHours= float(input ("How many overtime hours did you have this week?: "))
overtimeWage= (1.5*hourWage)
totalWeeklyPay= (hourWage*regularHours)+(overtimeHours*overtimeWage)
print("Your total weekly pay is: " ,totalWeeklyPay)
# What is your hourly wage?: 15000
# How many regular hours did you work this week?: 30
# How many overtime hours did you have this week?: 5
# Your total weekly pay is:  562500.0

