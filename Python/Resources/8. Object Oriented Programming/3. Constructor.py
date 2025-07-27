# Constructor in Python

# What is a Constructor?
'''
A constructor is a special type of method (function) used to initialize the instance members of a class.
When a class is created without a constructor, Python automatically provides a default constructor.
Every class must have a constructor, which is defined using the `__init__` method.
'''

# ----------------------------
# Types of Constructors
# ----------------------------
'''
1. Default Constructor (Non-Parameterized Constructor)
2. Parameterized Constructor
3. Copy Constructor
'''

# ----------------------------
# Default Constructor (Non-Parameterized Constructor)
# ----------------------------
'''
A default constructor does not take any arguments (except `self`).
It is used to initialize objects with default values.
'''

class DefaultConstructor:
    def __init__(self):  # Default constructor with no parameters
        print("Default Constructor Called")
    
    def display(self, name):
        print("Name:", name)

# Creating an object of the class, which will automatically call the constructor
default_constructor = DefaultConstructor()

default_constructor.display("Dennis Ritchie")  # Calling the display method

# ----------------------------
# Parameterized Constructor
# ----------------------------
'''
A parameterized constructor accepts arguments to initialize an object with specific values.
'''

class ParameterizedConstructor:
    def __init__(self, name):  # Constructor with a parameter
        self.name = name  # Assigning the parameter to an instance variable
        print("Parameterized Constructor Called")
    
    def display(self):
        print("Name:", self.name)

# Creating an object and passing a parameter to the constructor
parameterized_constructor = ParameterizedConstructor("Guido van Rossum")
parameterized_constructor.display()  # Displaying the name
