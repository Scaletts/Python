"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Project_08_page133.py
Problem:
      Write a script named copyfile.py. This script should prompt the user for the names of two text files.
        The contents of the first file should be input and written to the second file.



Solution:
    Display result
        Enter the input file name: ../fileTest/testCode.txt
        Enter the output file name: ../fileTest/test.txt
"""

inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")

inputFile = open(inName, 'r')
text = inputFile.read()

outFile = open(outName, 'w')
outFile.write(text)
outFile.close()
