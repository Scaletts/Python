"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_02_page_125.py
Problem:
     Write a code segment that opens a file for input and prints the number of four-letter words in the file.


Solution:
    Display result:
        Content first 4 characters: Hoàn

"""

textFile = open("../fileTest/myfile.txt", 'w', encoding='utf-8')
textFile.write("Hoàng là nhất")

textFile = open("../fileTest/myfile.txt", 'r', encoding='utf-8')
print("Content first 4 characters:", textFile.read(4))

textFile.close()
