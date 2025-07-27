# Tuple Datatype in Python

# What is a Tuple?
"""
Tuples are used to store multiple items in a single variable.
They are immutable, meaning once created, their values cannot be modified.
Tuples are faster than lists and are often used when data should remain unchanged.
They use parentheses () for definition.
They allow duplicate values.
"""

# Creating Tuples
tuple1 = (1, 2, 3, 4, 5)                   # Tuple with integers
tuple2 = ("apple", "banana", "cherry")       # Tuple with strings
tuple3 = (1, "orange", True, 3.14, "watermelon")  # Tuple with mixed data types

# Printing Tuples
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)

# ------------------------------
# Checking Type and Length of a Tuple
# ------------------------------

# Checking the type of a tuple
print("\nChecking Type of Tuple:")
print("Type of tuple1:", type(tuple1))
print("Type of tuple2:", type(tuple2))
print("Type of tuple3:", type(tuple3))

# Checking the length of a tuple
print("\nChecking Length of Tuple:")
print("Length of tuple1:", len(tuple1))
print("Length of tuple2:", len(tuple2))
print("Length of tuple3:", len(tuple3))

# Create a tuple with one element
tuple5 = ("apple",)  # Note the comma to denote a tuple
print("\nType of tuple5:", type(tuple5))

# ------------------------------
# Accessing Elements of a Tuple
# ------------------------------

print("\nAccessing Elements by Index:")
print("First element in tuple1:", tuple1[0])
print("Last element in tuple1:", tuple1[-1])
print("Elements from index 2 to end:", tuple1[2:])
print("Elements from index 1 onwards:", tuple1[1:])
print("Elements before index 2:", tuple1[:2])

# ------------------------------
# Tuple Concatenation
# ------------------------------

print("\nTuple Concatenation:")
tuple6 = (6, 7, 8)
tuple7 = tuple1 + tuple6
print("Concatenated tuple:", tuple7)

# ------------------------------
# Looping through a Tuple
# ------------------------------

print("\nLoop using Tuple:")
for element in tuple1:
    print(element)

# ------------------------------
# Creating a Tuple Using Constructor
# ------------------------------

print("\nCreating a Tuple Using tuple() Constructor:")
tuple4 = tuple(("apple", "banana", "cherry"))  # Double parentheses required
print("Tuple created with constructor:", tuple4)

# ------------------------------
# Tuple Methods (Manipulating Tuples)
# ------------------------------

# 1. count() → Returns the number of times a specific value appears in the tuple
print("\ncount() method:")
tuple5 = (1, 2, 3, 3, 4, 5)
print("Number of occurrences of 3:", tuple5.count(3))

# 2. index() → Returns the index of the first occurrence of a specific value
print("\nindex() method:")
print("Index of 3:", tuple5.index(3))
