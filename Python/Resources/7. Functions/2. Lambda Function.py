# Lambda Functions in Python

# What are Lambda Functions?
"""
Lambda functions are anonymous functions, meaning they are defined without a name.
They are defined using the 'lambda' keyword.
Lambda functions are often used for short, one-line functions.
They can take any number of arguments but can only have one expression.

Syntax:
lambda arguments: expression
"""

# Defining a Lambda Function
x = lambda a: a + 10  # Adds 10 to the given number
print(x(10))  # Output: 20

# Lambda Function with Two Arguments
y = lambda a, b: a * b  # Multiplies two numbers
print(y(2, 5))  # Output: 10

# Lambda Function with Three Arguments
z = lambda a, b, c: a + b + c  # Adds three numbers
print(z(1, 2, 3))  # Output: 6

# Using Lambda within a Function
def sample(n):
    return lambda a: a * n  # Returns a function that multiplies 'a' by 'n'

x = sample(2)
print(x(11))  # Output: 22
