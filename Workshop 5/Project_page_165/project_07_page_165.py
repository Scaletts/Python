"""
Author: DuongTruongTho
Date: 09/08/2021
Program: Project_07_page_165.py
Problem:
     Write a program that inputs a text file. The program should print the unique
     words in the file in alphabetical order.



Solution:
    
"""
with open('test.txt','r') as f:
	for line in f:
		print(set(line.split()))