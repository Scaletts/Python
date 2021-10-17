"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Project_12_page133.py
Problem:
     The Payroll Department keeps a list of employee information for each pay period in a text file.
        The format of each line of the file is the following:
                                <last name> <hourly wage> <hours worked>
        Write a program that inputs a filename from the user and prints to the terminal a report of the
        wages paid to the employees for the given period. The report should be in tabular format with
        the appropriate header. Each line should contain an employee�s name, the hours worked, and the
        wages paid for that period.



Solution:
    Display result
        Enter the file name: ../fileTest/data.txt
        Name            Hours      Total Pay
        Lambert            34          357.0
        Osborne            22          137.5
        Giacometti          5          503.5

"""

fileName = input("Enter the file name: ")

inputFile = open(fileName, 'r')

print("%-15s%6s%15s" % ("Name", "Hours", "Total Pay"))
for line in inputFile:
    dataList = line.split()
    name = dataList[0]
    hours = int(dataList[1])
    payRate = float(dataList[2])
    totalPay = hours * payRate
    print("%-15s%6s%15s" % (name, hours, totalPay))
