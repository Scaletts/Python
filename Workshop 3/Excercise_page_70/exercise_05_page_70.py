"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: excersice_05_page_70.py
Problem:
    Assume that the variable teststring refers to a string. Write a loop that prints each character in this string, followed by its ASCII value.
Solution:
    print(" -----------------------------------")
    print(" the 1st 128 ascii values...........")
    print("  ascii value     character    ")
    for asciiLoop in range(128):
    print("     " +str(asciiLoop) + "                  " + chr(asciiLoop)  )
    print(" -----------------------------------")
    print(" the 1st 128 ascii values...........")
    for asciiLoop in range(256):
    print( "     " +   str(asciiLoop) + "                  " + chr(asciiLoop)  )

    import random
    def testString():
        n = random.randint(0,25)
        strReturnStr = " "
        for i in range(n):
                asciiValue = 0
                while (int(asciiValue)<32):
                asciiValue = random.randint(32,127)
                strReturnStr = strReturnStr + chr(asciiValue)
        return(strReturnStr)
        def asciiDump(inbuff):
            n = len(inbuff)
            print("  Character         Ascii Value   ")
            for i in range(n):
                ch = inbuff[i]
                print(   ch   +    "         " + str(ord(ch)))
        strBuffStr = testString()
        asciiDump(strBuffStr)

    ....
"""
print(" -----------------------------------")
print(" the 1st 128 ascii values...........")
print("  ascii value     character    ")
for asciiLoop in range(128):
 print("     " +str(asciiLoop) + "                  " + chr(asciiLoop)  )
print(" -----------------------------------")
print(" the 1st 128 ascii values...........")
for asciiLoop in range(256):
 print( "     " +   str(asciiLoop) + "                  " + chr(asciiLoop)  )

import random
def testString():
    n = random.randint(0,25)
    strReturnStr = " "
    for i in range(n):
            asciiValue = 0
            while (int(asciiValue)<32):
             asciiValue = random.randint(32,127)
            strReturnStr = strReturnStr + chr(asciiValue)
    return(strReturnStr)
    def asciiDump(inbuff):
        n = len(inbuff)
        print("  Character         Ascii Value   ")
        for i in range(n):
            ch = inbuff[i]
            print(   ch   +    "         " + str(ord(ch)))
    strBuffStr = testString()
    asciiDump(strBuffStr)
