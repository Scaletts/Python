"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_01_page_125.py
Problem:
      Write a code segment that opens a file named myfile.txt for input and prints the number of lines in the file.


Solution:
    Display result:
        Content first 5 characters: Hoàng

"""

textFile = open("../fileTest/myfile.txt", 'w', encoding='utf-8')
textFile.write("Hoàng là nhất")

textFile = open("../fileTest/myfile.txt", 'r', encoding='utf-8')
print("Content first 5 characters:", textFile.read(5))

textFile.close()



