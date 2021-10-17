"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_03_page_125.py
Problem:
      Assume that a file contains integers separated by newlines. Write a code segment that opens the
        file and prints the average value of the integers.


Solution:
    Display result:
        Average: 5.0

"""

textFile = open("../fileTest/myfile.txt", 'w', encoding='utf-8')
for index in range(1, 10):
    textFile.write(str(index) + '\n')

textFile = open("../fileTest/myfile.txt", 'r', encoding='utf-8')
sum = 0
count = 0
for line in textFile:
    sum += int(line.strip())
    count += 1
average = sum/count

print("Average:", average)
