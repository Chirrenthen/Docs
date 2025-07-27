# Abstraction in Python

# What is Abstraction?
'''
Abstraction is a concept in programming that focuses on exposing only the necessary details while hiding the complex implementation details.
It allows users to interact with an object or a system through a simplified interface, without needing to understand the underlying complexity.
This helps in reducing the cognitive load on the user and promotes a cleaner and more organized code structure.
'''

# Types of Abstraction
'''
Thre are two types of using abstraction in Python,
1. Using Abstact Classes and interfaces
2. Abstraction using 2 different files or 'modules'
'''

# How to Implement Abstraction classes and interfaces
'''
It can be implemented by using abstract classes and interfaces
An abstract class is a class that is intended to be inherited by other classes and contains abstract methods that must be overridden in the derived class.
An interface is a set of methods that must be implemented by the derived class.
'''
# Example:
from abc import ABC, abstractmethod

# Abstract Class
class Laptop(ABC):
    @abstractmethod
    def boot_up(self):
        pass
    
    @abstractmethod
    def shut_down(self):
        pass

# Concrete Class 1
class Windows(Laptop):
    def boot_up(self):
        print("Windows11 is booting up...")
    
    def shut_down(self):
        print("Windows11 is shutting down...")

# Concrete Class 2
class MacOS(Laptop):
    def boot_up(self):
        print("MacOS is booting up...")
    
    def shut_down(self):
        print("MacOS is shutting down...")

# Using abstraction
windows_laptop = Windows()
windows_laptop.boot_up()
windows_laptop.shut_down()

mac_laptop = MacOS()
mac_laptop.boot_up()
mac_laptop.shut_down()

# Abstraction using 'modules'
'''
Here we create a file called a 'module' and import the classes.
Thus we only show the nessary details while hiding the others.
'''

# Example
from Factorial import * # Importing all classes present in Factorial

obj = Factorial()
print(obj.fact(5))
