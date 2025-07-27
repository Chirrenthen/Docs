# File Handling in Python

# What is File Handling?
'''
Python too supports file handling and allows users to handle files. ie, to read and write files.
Each line of code includes a sequence of characters and they form a file.
File is an external storage on a hard disk from where data can be stored and retrived.
'''

# ----------------------------
# 1. Opening a File
# ----------------------------
'''
Before working with files, you have to open the file.
To open a file, we use the open() function.
The open() function takes two parameters: the filename and the mode.

Syntax:
file = open(filename, mode)
'''

# ----------------------------
# 2. Modes
# ----------------------------
'''
There are 3 main modes for opening a file:
1. "r" - Opens a file for reading (default mode).
2. "w" - Opens a file for writing. Creates a new file if it doesn't exist or truncates it if it does.
3. "a"- Opens a file for appending. Creates a new file if it doesn't exist.

Apart from these, there are 5 more modes:
4. "r+" - Opens a file for both reading and writing. The file must exist.
5. "w+" - Opens a file for both writing and reading. Creates a new file if it doesn't exist or truncates it if it does.
6. "a+" - Opens a file for both appending and reading. Creates a new file if it doesn't exist.
7. "x" - Opens a file for exclusive creation. Fails if the file already exists.
8. "xt" - Opens a file for exclusive creation in text mode.
'''

# 1. "r" Mode
'''
To open a file in read mode, use the "r" mode.
'''
print("read(r) mode:")
with open("Resources/10. File Handling/2. File.py", "r") as file:
    print(file.read())

# 2. "w" Mode
'''
To open a file in write mode, use the "w" mode.
Run this file and open the file location, and you will see the "file.txt" is created.
'''
print("\nwrite(w) mode:")
with open("Resources/10. File Handling/file.txt", "w") as file:
    file.write("""
    Hello World! 
    This is an example for Write mode """) 

# 3. "a" Mode
'''
To open a file in append mode, use the "a" mode.
'''
print("\nappend(a) mode:")
with open("Resources/10. File Handling/file.txt", "a") as file:
    file.write("""
    This is an example for Append mode""")

# 4. "r+" Mode
'''
To open a file in read and write mode, use the "r+" mode.
'''
print("\nread and write(r+) mode:")
with open("Resources/10. File Handling/file.txt", "r+") as file:
    print(file.read())
    file.write("""
    This is an example for Read and Write mode""")

# 5. "w+" Mode
'''
print("\nwrite and read(w+) mode:")
To open a file in write and read mode, use the "w+" mode.
'''
with open("Resources/10. File Handling/file.txt", "w+") as file:
    print(file.read())
    file.write("""
    This is an example for Write and Read mode""")

# 6. "a+" Mode
'''
To open a file in append and read mode, use the "a+" mode.
'''
print("\nappend and read(a+) mode:")
with open("Resources/10. File Handling/file.txt", "a+") as file:
    print(file.read())
    file.write("""
    This is an example for Append and Read mode""")
