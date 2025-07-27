# Variables and Getting Types in Python

# What are Variables?
"""
Variables are used to store data in a computer's memory.
There are two types of variables in Python:

1. Global Variables:
   - These variables are accessible from anywhere in the program.
   - They are defined outside any function.

2. Local Variables:
   - These variables are accessible only within the function in which they are created.
"""

# Example of Global Variables
# Declaring variables outside a function (Global Scope)
a = 10      # Integer
b = "20"    # String
c = 30.0    # Float

def function():
    # Example of Local Variables
    d = 40      # Integer
    e = "50"    # String
    f = 60.0    # Float

    # Accessing Global Variables
    print("\nCalling Global Variables:")
    print(a, b, c)
    
    # Accessing Local Variables
    print("\nCalling Local Variables:")
    print(d, e, f)

# Calling the function to demonstrate variable scope
function()

# ----------------------------
# Assigning Values to Variables
# ----------------------------
"""
There are two ways to assign values to variables in Python:

1. Multiple values to multiple variables
2. A single value to multiple variables
"""

g, h, i = 1, 2, 3   # Assigning multiple values to multiple variables
j = k = l = 1       # Assigning a single value to multiple variables

# ----------------------------
# Getting the Type of a Variable
# ----------------------------
"""
The type() function returns the data type of a variable.
It helps in identifying the type of value stored in a variable.
"""

print("\nGetting the type of a variable:")
print("Type of variable a:", type(a))
print("Type of variable b:", type(b))
print("Type of variable c:", type(c))
