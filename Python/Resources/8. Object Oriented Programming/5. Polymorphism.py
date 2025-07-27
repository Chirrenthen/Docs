# Polymorphism in Python

# What is Polymorphism?
''' 
It refers to multiple forms of an object.
By uing this we can execute multiple functionalities with same method name.

There are two types of polymorphism:

1. Method Overloading or Runtime Polymorphism
2. Method Overriding or Compile Time Polymorphism
'''

# ------------------------------
# Method Overloading or Runtime
# ------------------------------

# What is Method Overloading?
'''
It has the same function name, same parameters but present in different class.
'''

class Windows11:
    def OS(self):
        print("I am Windows 11")

class MacOS:
    def OS(self):
        print("I am MacOS")

print("\nMethod Overloading")
I = Windows11()
I.OS()

J = MacOS()
J.OS()

# ------------------------------
# Method Overriding or Compiletime
# ------------------------------

# What is Method Overriding?
'''
It has the same function name but has different parameters
'''

def WindowsOS(a,b):
    p = a*b
    print(p)

def WindowsOS(a,b,c):
    s = a+b+c
    print(s)

WindowsOS(8,10,11)

