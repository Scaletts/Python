"""
Author: DuongTruongTho
Date: 09/08/2021
Program: Exersice_03_page_158.py
Problem:
      Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
        expressions that perform the following tasks:
        a. Replace the value at the key 'b' in data with that value’s negation.
        b. Add the key/value pair 'c':40 to data.
        c. Remove the value at key 'b' in data, safely.
        d. Print the keys in data in alphabetical order

Solution:
    a) x = data.get("b")
       data["b"]=-x
       print(data)
   (b) data.update({"c":40})
       print(data)
   (c) data.pop("b")
       print(data)
   (d)  dict_keys = data.keys()
        keyList = []
        for key in dict_keys:
           #print(key)
           keyList.append(key)
        keyList.sort()
        print(keyList)
    

    {'b': -20, 'a': 35}
    {'b': -20, 'a': 35, 'c': 40}
    {'a': 35, 'c': 40}
    ['a']
    ['a', 'c']
"""
data={'b':20, 'a':35}
x =data.get("b")
data["b"]=-x
print(data)



data.update({"c":40})
print(data)



data.pop("b")

print(data)



dict_keys = data.keys()

keyList = []

for key in dict_keys:

           #print(key)
    keyList.append(key)

    keyList.sort()

    print(keyList)