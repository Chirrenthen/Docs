# Functions in Python

# What are Functions?
"""
Functions are reusable blocks of code that perform specific tasks.
They are created using the 'def' keyword and executed when called.
Functions help in modular programming, making the code more readable and maintainable.
"""

# Defining a simple function
def greet():
    """This function prints a greeting message."""
    print("Hello from a function")

# Calling the function
greet()

# ---------------------------------
# Arguments and Parameters in Functions
# ---------------------------------

"""
Arguments: Values passed to the function when calling it.
Parameters: Variables declared in the function definition to accept arguments.
"""

def greet_user(name):
    """This function greets the user by name."""
    print("Hello " + name)

# Calling the function with an argument
greet_user("Python")

# ---------------------------------
# Function with Return Values
# ---------------------------------

"""
A function can return a value using the 'return' statement.
This allows the function to send back a result to the caller.
"""

def multiply_by_five(x):
    """Returns the given number multiplied by 5."""
    return 5 * x

# Calling the function and printing the result
print(multiply_by_five(3))

# ---------------------------------
# Recursion in Python
# ---------------------------------

"""
Recursion is a technique where a function calls itself.
It is often used for problems that can be broken down into smaller subproblems.
"""

def recursive_sum(n):
    """Calculates the sum of numbers from n to 0 using recursion."""
    if n > 0:
        result = n + recursive_sum(n - 1)
        print(result)  # Printing intermediate results for understanding
    else:
        result = 0
    return result

print("Recursion Example Results:")
recursive_sum(5)

# ---------------------------------
# Factorial Using Recursion
# ---------------------------------

def factorial(n):
    """Returns the factorial of a number using recursion."""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the factorial function
print("Factorial of 5:", factorial(5))
