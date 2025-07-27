# Class and Objects in Python

# What are Classes?
"""
Classes are user-defined data types that act as blueprints or templates for creating objects.
They define the structure and behavior of objects, which are instances of the class.
Classes provide a way to group related data and behavior together, making it easier to manage and reuse code.

Syntax:
class ClassName:
    # statements
"""

# What are Objects?
'''
They are real world entities which consists of state and behavior.
State represents the characteristics of an object
Behavior represents the functionality of an object.
It is an instance of a class.

Syntax:
objectName = ClassName(arguments)
'''

# Example using Classes and Objects
class ProgrammingLanguage:
    language = "Python"
    founder = "Guido van Rossum"
    year = "1991"
    def display(self):
        print("I am function")

# Creating Objects
python = ProgrammingLanguage()

# Accessing Attributes
print("Language:", python.language)
print("Founder:", python.founder)
print("Year:", python.year)

# Calling Methods
python.display()

# Note:
'''
The self will be helpful to access the attributes(variables) and methods of the class.
'''

# ----------------------------
# The __init__() Function
# ----------------------------
'''
This function is used to assgning the values to the variables in the class.
'''
# Example:
class ProgrammingLanguage:
    def __init__(self, language, founder, year):
        self.language = language
        self.founder = founder
        self.year = year
        print("\n __init__() function called")


python = ProgrammingLanguage("C - programming", "Dennis Ritchie", "1963")

print("Language:", python.language)
print("Founder:", python.founder)
print("Year:", python.year)