"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_04_page_73.py
Problem:
    Write a loop that outputs the numbers in a list named salaries. The outputs should be
    formatted in a column that is right-justified, with a field width of 12 and a precision of 2.
Solution:
    salaries = [ 3.142, 3.33, 2.723, 2.46, 5.34, 7.05, 7.53, 12.25, 18.21, 21.18, 24.32, 32.24, 24.36, 36.24, 32.36, 36.32, 35.42, 42.36, 48.55, 53.24, 69.77, 77.69,89.03, 99.99]
    print(" salary amounts:")
    N = len(salaries)
    for i in range(N):
        outbuff = ("%12.2f" %salaries[i])
        print(" Salary # " +str(i+1)+ " of " +  str(N) + " is : "+outbuff)
    ....
"""
salaries = [ 3.142, 3.33, 2.723, 2.46, 5.34, 7.05, 7.53, 12.25, 18.21, 21.18, 24.32, 32.24, 24.36, 36.24, 32.36, 36.32, 35.42, 42.36, 48.55, 53.24, 69.77, 77.69,89.03, 99.99]
print(" salary amounts:")
N = len(salaries)
for i in range(N):
    outbuff = ("%12.2f" %salaries[i])
    print(" Salary # " +str(i+1)+ " of " +  str(N) + " is : "+outbuff)

# salary amounts:
#  Salary # 1 of 24 is :         3.14
#  Salary # 2 of 24 is :         3.33
#  Salary # 3 of 24 is :         2.72
#  Salary # 4 of 24 is :         2.46
#  Salary # 5 of 24 is :         5.34
#  Salary # 6 of 24 is :         7.05
#  Salary # 7 of 24 is :         7.53
#  Salary # 8 of 24 is :        12.25
#  Salary # 9 of 24 is :        18.21
#  Salary # 10 of 24 is :        21.18
#  Salary # 11 of 24 is :        24.32
#  Salary # 12 of 24 is :        32.24
#  Salary # 13 of 24 is :        24.36
#  Salary # 14 of 24 is :        36.24
#  Salary # 15 of 24 is :        32.36
#  Salary # 16 of 24 is :        36.32
#  Salary # 17 of 24 is :        35.42
#  Salary # 18 of 24 is :        42.36
#  Salary # 19 of 24 is :        48.55
#  Salary # 20 of 24 is :        53.24
#  Salary # 21 of 24 is :        69.77
#  Salary # 22 of 24 is :        77.69
#  Salary # 23 of 24 is :        89.03
#  Salary # 24 of 24 is :        99.99