"""
Author: Dương Trường Thọ
Date: 11/07/2021
Program: project_03_page_62-63.py
Problem:
    
    Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
    like to buy LP record albums. The store rents new videos for $3.00 a night, and
    oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
    can use to calculate the total charge for a customer’s video rentals. The program
    should prompt the user for the number of each type of video and output the total
    cost.
    
Solution:
    ....
"""


# Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums. The store rents new videos for $3.00 a night, and
  #oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals. The program
  #should prompt the user for the number of each type of video and output the total cost.
videos = int(input("Enter the number of new videos: "))
oldies = int(input("Enter the number of oldies: "))
result = (videos *3.00) + (oldies *2.00)
print("The total cost is","$",result)
#Enter the number of new videos: 5
#Enter the number of oldies: 5
#The total cost is $ 25.0

