"""
Author: DuongTruongTho
Date: 02/09/2021
Program: casestudy_Gathering Information from a File System_page_183.py
Problem:
    CaSe StuDy: Gathering Information from a File System
    Modern file systems come with a graphical browser, such as Microsoft’s Windows
    Explorer or Apple’s Finder. These browsers allow the user to navigate to files or
    folders by selecting icons of folders, opening these by double-clicking, and selecting
    commands from a drop-down menu. Information on a folder or a file, such as the size
    and contents, is also easily obtained in several ways.
    Users of terminal-based user interfaces (see Chapter 2) must rely on entering the
    appropriate commands at the terminal prompt to perform these functions. In this
    case study, we develop a simple terminal-based file system navigator that provides
    some information about the system. In the process, we will have an opportunity to
    exercise some skills in top-down design and recursive design.
    request
    Write a program that allows the user to obtain information about the file system.
    analysis
    File systems are tree-like structures, as shown in Figure 6-5.
Solution:
    1 List the current directory
    2 Move up
    3 Move down
    4 Number of files in the directory
    5 Size of the directory in bytes
    6 Search for a filename
    7 Quit the program
    Enter a number:

"""
import os, os.path
QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')
MENU = """1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory
5 Size of the directory in bytes
6 Search for a filename
7 Quit the program"""
def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break
def acceptCommand():
    """Inputs and returns a legitimate command number."""
    command = input("Enter a number: ")
    if command in COMMANDS:
        return command
    else:
        print("Error: command not recognized")
        return acceptCommand()
def runCommand(command):
    """Selects and runs a command."""
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is", \
        countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is", \
        countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
def listCurrentDir(dirName):
    """Prints a list of the cwd's contents."""
    lyst = os.listdir(dirName)
    for element in lyst: print(element)
def moveUp():
    """Moves up to the parent directory."""
    os.chdir("..")
def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
        os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")
def countFiles(path):
    """Returns the number of files in the cwd and all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count
def countBytes(path):
    """Returns the number of bytes in the cwd and all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count
def findFiles(target, path):
    """Returns a list of the filenames that contain the target string in the cwd and all its subdirectories."""
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
            else:
                os.chdir(element)
                files.extend(findFiles(target, os.getcwd()))
                os.chdir("..")
        return files
if __name__ == "__main__":
    main()