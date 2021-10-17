"""
Author: DuongTruongTho
Date: 09/08/2021
Program: Project_02_page_165.py
Problem:
    Write a program that allows the user to navigate the lines of text in a file. The
    program should prompt the user for a filename and input the lines of text into a
    list. The program then enters a loop in which it prints the number of lines in the
    file and prompts the user for a line number. Actual line numbers range from 1 to
    the number of lines in the file. If the input is 0, the program quits. Otherwise, the
    program prints the line associated with that number
     



Solution:
    
"""
enterfile=input("Enter the file name:")
with open(enterfile) as f:
    lines=[line.rstrip() for line in f]
print("The number of lines in this txt .file is",len(lines))
while True:
    num=int(input("Please enter a line number or press 0 to quit:"))
    if num>0 and num< len(lines) +1:
        print(lines[num-1])
    elif num==0:
        print('Thanks for using the program.')
        break