"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: project_07_page_99.py
Problem:
    Teachers in most school districts are paid on a schedule that provides a salary
    based on their number of years of teaching experience. For example, a beginning
    teacher in the Lexington School District might be paid $30,000 the first year. For
    each year of experience after this first year, up to 10 years, the teacher receives a
    2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for teachers in a school district. The inputs are the starting
    salary, the percentage increase, and the number of years in the schedule. Each row
    in the schedule should contain the year number and the salary for that year.
Solution:
    
    ....
"""
startSalary = int(input("Please enter beginning salary: "))
percentIncrease = (float(input("Please enter percentage increase: ")) / 100)
numberYears = int(input("Please enter number of years in schedule: "))
for i in range(1,numberYears+1):
    print("{} year salary is  {:0.2f}".format(
        i, 
        startSalary * ((1 + percentIncrease) ** (i - 1))))