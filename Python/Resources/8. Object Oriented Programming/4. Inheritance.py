# Inheritance in Python
'''
All the properties(variables) and functions(methods) of the parent class are inherited to the child class.

Parent Class:
It is the class which gives the properties and functions to another class.
It is also called as Base Class or Super Class.

Child Class:
It is the class which inherits all the properties and functions from the parent class.
It is also called as Sub Class, Derived Class and Extended Class.

Different Types of Inheritance:
1. Single Level Inhertance -> One parent class and one child class.
2. Multi-level Inheritance -> Multiple parents at different levels and one child class.
3. Multiple Inheritance -> Multiple parents at the same level and one child class.
4. Hierarchical Inheritance -> Single parent and multiple child classes.
5. Hybrid Inheritance -> Consists of Multiple inheritance and Hierarchical inheritance.
'''
# ----------------------------
# Single Level Inheritance
# ----------------------------
'''
  Parent Class
      ⬇️
  Child Class
'''
class Laptop:
    def VSCode(self):
        print("I am VS Code")

class Python(Laptop):
    def Run(self):
        print("I am Python in VS Code")

print("Single Level Inheritance")
I = Python()
I.VSCode()
I.Run()

# ----------------------------
# Multi-level Inheritance
# ----------------------------
'''
  Parent Class
      ⬇️
  Child Class
      ⬇️
  Grand Child Class
'''
class Windows:
    def WindowsOS(self):
        print("I am Windows OS")

class Laptop(Windows):
    def VSCode(self):
        print("I am VS Code running on Windows OS")

class Python(Laptop):
    def Run(self):
        print("I am Python running in VS Code")

print("\nMulti-level Inheritance")
I = Python()
I.WindowsOS()
I.VSCode()
I.Run()

# ----------------------------
# Multiple Inheritance
# ----------------------------
'''
  Parent Class 1  Parent Class 2
       ⬇️             ⬇️
           Child Class
'''
class Apple:
    OS = ""
    def MacOS(self):
        print(self.OS)

class Google:
    Browser = ""
    def Chrome(self):
        print(self.Browser)

class Python(Apple, Google):
    def Run(self):
        print(self.OS)
        print(self.Browser)
        print("I am Python running in " + self.Browser + " on " + self.OS)

print("\nMultiple Inheritance")
I = Python()
I.OS = "Mac OS"
I.Browser = "Chrome"  
I.Run()

# ----------------------------
# Hierarchical Inheritance
# ----------------------------
'''
          Parent Class
               ⬇️
  Child Class 1  Child Class 2
'''
class Laptop:
    def OS(self):
        print("I am Laptop")

class Windows11(Laptop):
    def windows(self):
        print("I am Windows 11 running on Laptop")

class MacOS(Laptop):
    def mac(self):
        print("I am MacOS running on Laptop")

print("\nHierarchical Inheritance") 
I = Windows11()
I.OS()
I.windows()

J = MacOS()
J.OS()
J.mac()

# ----------------------------
# Hybrid Inheritance
# ----------------------------
'''
          Parent Class                                             Parent Class
               ⬇️                                                      ⬇️
  Child Class 1  Child Class 2             (or)            Child Class 1  Child Class 2
        ⬇️                                                                    ⬇️
  Child Class 3                                                           Child Class 3
'''
class Laptop:
    def OS(self):
        print("I am Laptop")

class Windows11(Laptop):
    def windows(self):
        print("I am Windows 11 running on Laptop")

class MacOS(Laptop):
    def mac(self):
        print("I am MacOS running on Laptop")

class ProgrammingLanguage(Windows11):
    def Run(self):
        self.OS()
        self.windows()
        print("I am a Programming Language running in Laptop")

print("\nHybrid Inheritance")
I = ProgrammingLanguage()
I.Run()
