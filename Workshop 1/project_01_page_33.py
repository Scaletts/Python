"""""
Author: Duong Truong Tho
Date: 04/07/2021
Program: project_01_page_33.py
Problem:
    1. Open a Python shell, enter the following expressions, and observe the results:
    a. 8
    b. 8 * 2
    c. 8 ** 2
    d. 8/12
    e. 8 // 12
    f. 8/0
    2. Write a Python program that prints (displays) your name, address, and telephone number.
    3. Evaluate the following code at a shell prompt: print ("Your name is", name).Then assign name an appropriate value, and evaluate the statement again.
    4. Open an IDLE window, and enter the program from Figure 1-7 that computes the area of a rectangle. Load the program into the shell by pressing the F5 key,
    and correct any errors that occur. Test the program with different inputs by
    running it at least three times.
    5. Modify the program of Project 4 to compute the area of a triangle. Issue the appropriate prompts for the triangle’s base and height, and change the names of
    the variables appropriately. Then, use the formula .5 * base * height to compute the area. Test the program from an IDLE window.
    6. Write and test a program that computes the area of a circle. This program should request a number representing a radius as input from the user. It should use the formula
    3.14 * radius ** 2 to compute the area and then output this result suitably labeled.
    7. Write and test a program that accepts the user’s name (as text) and age (as a number)
    as input. The program should output a sentence containing the user’s name and age.
    8. Enter an input statement using the input function at the shell prompt. When the
    prompt asks you for input, enter a number. Then, attempt to add 1 to that number, observe the results, and explain what happened.
    9. Enter an input statement using the input function at the shell prompt. When the prompt asks you for input, enter your first name, observe the results, and explain
    what happened.
    10. Enter the expression help() at the shell prompt. Follow the instructions to browse the topics and modules.
    Solution:
    ....
"""
#1.Open a Python shell, enter the following expressions, and observe the results:
#a.
from typing import NamedTuple


print(8)
#b.
print(8*2)
#c.
print(8**2)
#d.
print(8/12)
#e.
print(8//12)
#f.
#print(8/0)
try:
    print(8/0)
except ZeroDivisionError:
    print ("không hợp lệ")

#2.Write a Python program that prints (displays) your name, address, and telephone number.
print("Name: Dương Trường Thọ")
print("Address: Phú Danh - Hra - Mang Yang - Gia Lai")
print("Phone: 03441181810")

#3. Evaluate the following code at a shell prompt: print ("Your name is", name).Then assign name an appropriate value, and evaluate the statement again.
try:
    print ("Your name is", NamedTuple)
except NameError:
    name="Dương Trường Thọ"
    print("Your name is", name)
#print ("Your name is", name)
#NameError: name 'name' is not defined xãy ra lỗi name chưa được định nghĩa

#4 Open an IDLE window, and enter the program from Figure 1-7 that computes the area of a rectangle. Load the program into the shell by pressing the F5 key,and correct any errors that occur. Test the program with different inputs byrunning it at least three times.
width = int(input("Enter with width: "))
height = int(input("Enter with height: "))
area = width * height
print("The area is", area, "square units.")
# testtime1 
#Enter with width: 5
#Enter with height: 5
#The area is 25 square units.

#testtime2
#Enter with width: 6
#Enter with height: 6
#The area is 36 square units.

#testtime3
#Enter with width: 5
#Enter with height: 7
#The area is 35 square units.

#5 Modify the program of Project 4 to compute the area of a triangle. Issue the appropriate prompts for the triangle’s base and height, and change the names ofthe variables appropriately. Then, use the formula .5 * base * height to compute the area. Test the program from an IDLE window.
base = float(input("Enter with base: "))
height = float(input("Enter with height: "))
area =  0.5*base * height
print("The area is", area, "square units.")
#Enter with base: 5
#Enter with height: 5
#The area is 12.5 square units.

#6 Write and test a program that computes the area of a circle. This program should request a number representing a radius as input from the user. It should use the formula 3.14 * radius ** 2 to compute the area and then output this result suitably labeled.
from math import pi
r = float(input ("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
#Input the radius of the circle : 5
#The area of the circle with radius 5.0 is: 78.53981633974483

#7 Write and test a program that accepts the user’s name (as text) and age (as a number) as input. The program should output a sentence containing the user’s name and age.
name = (input("Enter your name: "))
age = int(input("Enter your age: "))
print(name, "is", age, "years old.")
#Enter your name: Dương Trường Thọ
#Enter your age: 20
#Dương Trường Thọ is 20 years old.

#8 Enter an input statement using the input function at the shell prompt. When theprompt asks you for input, enter a number. Then, attempt to add 1 to that number, observe the results, and explain what happened.
num = (input('Number: '))
num = num + 1
print(num)
# num = num + 1
#TypeError: can only concatenate str (not "int") to str (The error “typeerror: can only concatenate str (not “int”) to str” is raised when you try to concatenate a string and an integer)
#corret code 
#num = (input('Number: '))
#num = num + 1
#print(num)
#Number: 5
#6

#9 Enter an input statement using the input function at the shell prompt. When the prompt asks you for input, enter your first name, observe the results, and explain what happened
name=input("Enter your first name :")
print(name)
#Enter your first name :Thọ  
#Thọ
#No error

#10 Enter the expression help() at the shell prompt. Follow the instructions to browse the topics and modules.
help()
# Welcome to Python 3.9's help utility!

# If this is your first time using Python, you should definitely check out
# the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

# Enter the name of any module, keyword, or topic to get help on writing
# Python programs and using Python modules.  To quit this help utility and
# return to the interpreter, just type "quit".

# To get a list of available modules, keywords, symbols, or topics, type
# "modules", "keywords", "symbols", or "topics".  Each module also comes
# with a one-line summary of what it does; to list the modules whose name
# or summary contain a given string such as "spam", type "modules spam".

# help> topics

# Here is a list of available topics.  Enter any topic name to get more help.

# ASSERTION           DELETION            LOOPING             SHIFTING
# ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
# ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
# ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
# AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
# BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
# BINARY              EXECUTION           NONE                STRINGS
# BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
# BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
# CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
# CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
# CLASSES             FRAMES              PACKAGES            TUPLES
# CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
# COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
# COMPLEX             IMPORTING           PRIVATENAMES        UNARY
# CONDITIONAL         INTEGER             RETURNING           UNICODE
# CONTEXTMANAGERS     LISTLITERALS        SCOPING
# CONVERSIONS         LISTS               SEQUENCEMETHODS
# DEBUGGING           LITERALS            SEQUENCES

# help> modules

# Please wait a moment while I gather a list of all available modules...

# __future__          _threading_local    genericpath         runpy
# _abc                _tkinter            getopt              sched
# _aix_support        _tracemalloc        getpass             secrets
# _ast                _uuid               gettext             select
# _asyncio            _warnings           glob                selectors
# _bisect             _weakref            graphlib            setuptools
# _blake2             _weakrefset         gzip                shelve
# _bootlocale         _winapi             hashlib             shlex
# _bootsubprocess     _xxsubinterpreters  heapq               shutil
# _bz2                _zoneinfo           hmac                signal
# _codecs             abc                 html                site
# _codecs_cn          aifc                http                smtpd
# _codecs_hk          antigravity         idlelib             smtplib
# _codecs_iso2022     argparse            imaplib             sndhdr
# _codecs_jp          array               imghdr              socket
# _codecs_kr          ast                 imp                 socketserver
# _codecs_tw          asynchat            importlib           sqlite3
# _collections        asyncio             inspect             sre_compile
# _collections_abc    asyncore            io                  sre_constants
# _compat_pickle      atexit              ipaddress           sre_parse
# _compression        audioop             itertools           ssl
# _contextvars        base64              json                stat
# _csv                bdb                 keyword             statistics
# _ctypes             binascii            lib2to3             string
# _ctypes_test        binhex              linecache           stringprep
# _datetime           bisect              locale              struct
# _decimal            builtins            logging             subprocess
# _distutils_hack     bz2                 lzma                sunau
# _elementtree        cProfile            mailbox             symbol
# _functools          calendar            mailcap             symtable
# _hashlib            cgi                 marshal             sys
# _heapq              cgitb               math                sysconfig
# _imp                chunk               mimetypes           tabnanny
# _io                 cmath               mmap                tarfile
# _json               cmd                 modulefinder        telnetlib
# _locale             code                msilib              tempfile
# _lsprof             codecs              msvcrt              test
# _lzma               codeop              multiprocessing     textwrap
# _markupbase         collections         netrc               this
# _md5                colorsys            nntplib             threading
# _msi                compileall          nt                  time
# _multibytecodec     concurrent          ntpath              timeit
# _multiprocessing    configparser        nturl2path          tkinter
# _opcode             contextlib          numbers             token
# _operator           contextvars         opcode              tokenize
# _osx_support        copy                operator            trace
# _overlapped         copyreg             optparse            traceback
# _peg_parser         crypt               os                  tracemalloc
# _pickle             csv                 parser              tty
# _py_abc             ctypes              pathlib             turtle
# _pydecimal          curses              pdb                 turtledemo
# _pyio               dataclasses         pickle              types
# _queue              datetime            pickletools         typing
# _random             dbm                 pip                 unicodedata
# _sha1               decimal             pipes               unittest
# _sha256             difflib             pkg_resources       urllib
# _sha3               dis                 pkgutil             uu
# _sha512             distutils           platform            uuid
# _signal             doctest             plistlib            venv
# _sitebuiltins       email               poplib              warnings
# _socket             encodings           posixpath           wave
# _sqlite3            ensurepip           pprint              weakref
# _sre                enum                profile             webbrowser
# _ssl                errno               project_01_page_33  winreg
# _stat               excercise_01_page_29 pstats              winsound
# _statistics         excercise_01_page_30 pty                 wsgiref
# _string             excercise_01_page_5 py_compile          xdrlib
# _strptime           excercise_01_page_9 pyclbr              xml
# _struct             faulthandler        pydoc               xmlrpc
# _symtable           filecmp             pydoc_data          xxsubtype
# _testbuffer         fileinput           pyexpat             zipapp
# _testcapi           fnmatch             queue               zipfile
# _testconsole        formatter           quopri              zipimport
# _testimportmultiple fractions           random              zlib
# _testinternalcapi   ftplib              re                  zoneinfo
# _testmultiphase     functools           reprlib
# _thread             gc                  rlcompleter

# Enter any module name to get more help.  Or, type "modules spam" to search
# for modules whose name or summary contain the string "spam".


