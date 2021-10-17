"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Project_09_page133.py
Problem:
        Write a script named numberlines.py. This script creates a program listing from a source program.
        This script should prompt the user for the names of two files. The input filename could be the name
        of the script itself, but be careful to use a different output filename! The script copies the lines
        of text from the input file to the output file, numbering each line as it goes. The line numbers should
        be right-justified in 4 columns, so that the format of a line in the output file looks like this example:

         This is the first line of text.



Solution:
    Display result
        Enter the input file name: ../fileTest/testCode.txt
        Enter the output file name: ../fileTest/test9.txt
"""

file_input = input("Enter the input file name: ")
output = input("Enter the output file name: ")

outFile = open(output, 'w')

with open(file_input, 'r') as file:
    index = 1
    for line in file:
        print(line)
        outFile.write("%d> "%index + line)
        index += 1
outFile.close()
