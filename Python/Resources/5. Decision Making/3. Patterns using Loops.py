"""
---------------------------------------------------
        Patterns using Loops in Python
---------------------------------------------------

This script demonstrates a wide variety of patterns printed using loops.
The patterns are organized into the following sections:

--- 1. Basic Patterns ---
    - Right-angle Triangle Pattern
    - Upside Down Right-angle Triangle Pattern
    - Inverted Right-angle Triangle Pattern
    - Inverted Upside Down Right-angle Triangle Pattern
    - Rectangle Pattern
    - Square Pattern

--- 2. Advanced Patterns ---
    - Diamond Pattern
    - Hill Pattern
    - Upside Down Hill Pattern
    - Pyramid Pattern
    - Inverted Pyramid Pattern
    - Butterfly Pattern

--- 3. Number Patterns ---
    - Number Right Angle Triangle Pattern (Sequential Numbers)
    - Odd Number Right Angle Triangle Pattern
    - Same Number Right Angle Triangle Pattern
    - Number Right Angle Triangle Pattern (Aligned Right)
    - Floyd's Triangle
    - Pascal's Triangle

--- 4. Additional Patterns ---
    - Hollow Square Pattern
    - Hollow Rectangle Pattern
    - Hollow Pyramid Pattern
    - Hourglass Pattern
---------------------------------------------------
"""

# ===============================
# 1. Basic Patterns
# ===============================

print("1. Basic Patterns")

# 1.1. Right-angle Triangle Pattern
print("\nRight-angle Triangle Pattern:")
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# 1.2. Upside Down Right-angle Triangle Pattern
print("\nUpside Down Right-angle Triangle Pattern:")
rows = 5
for i in range(rows):
    for j in range(rows - i):
        print("*", end=" ")
    print()

# 1.3. Inverted Right-angle Triangle Pattern
print("\nInverted Right-angle Triangle Pattern:")
rows = 5
for i in range(rows):
    # Leading spaces for right alignment
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

# 1.4. Inverted Upside Down Right-angle Triangle Pattern
print("\nInverted Upside Down Right-angle Triangle Pattern:")
rows = 5
for i in range(rows):
    # Leading spaces increase with each row
    for j in range(i):
        print(" ", end=" ")
    for j in range(rows - i):
        print("*", end=" ")
    print()

# 1.5. Rectangle Pattern
print("\nRectangle Pattern:")
height = 5
width = 9
for i in range(height):
    for j in range(width):
        print("*", end=" ")
    print()

# 1.6. Square Pattern
print("\nSquare Pattern:")
side = 10
for i in range(side):
    for j in range(side):
        print("*", end=" ")
    print()

# ===============================
# 2. Advanced Patterns
# ===============================

print("\n2. Advanced Patterns")

# 2.1. Diamond Pattern
print("\nDiamond Pattern:")
size = 10
symbol = "*"
# Upper part of diamond
for i in range(size - 1):
    for j in range(i, size):
        print(" ", end=" ")
    for j in range(i + 1):
        print(symbol, end=" ")
    for j in range(i):
        print(symbol, end=" ")
    print()
# Lower part of diamond
for i in range(size):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, size):
        print(symbol, end=" ")
    for j in range(i, size - 1):
        print(symbol, end=" ")
    print()

# 2.2. Hill Pattern
print("\nHill Pattern:")
size = 10
for i in range(size - 1):
    for j in range(i, size):
        print(" ", end=" ")
    for j in range(i + 1):
        print(symbol, end=" ")
    for j in range(i):
        print(symbol, end=" ")
    print()

# 2.3. Upside Down Hill Pattern
print("\nUpside Down Hill Pattern:")
for i in range(size):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, size):
        print(symbol, end=" ")
    for j in range(i, size - 1):
        print(symbol, end=" ")
    print()

# 2.4. Pyramid Pattern
print("\nPyramid Pattern:")
rows = 5
for i in range(rows):
    # Print leading spaces for pyramid shape
    for j in range(rows - i - 1):
        print(" ", end=" ")
    # Print increasing stars; odd number per row
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()

# 2.5. Inverted Pyramid Pattern
print("\nInverted Pyramid Pattern:")
for i in range(rows, 0, -1):
    # Leading spaces increase as rows decrease
    for j in range(rows - i):
        print(" ", end=" ")
    # Print stars in decreasing order
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

# 2.6. Butterfly Pattern
print("\nButterfly Pattern:")
n = 5
# Upper half
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
# Lower half
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# ===============================
# 3. Number Patterns
# ===============================

print("\n3. Number Patterns")

# 3.1. Number Right Angle Triangle Pattern (Sequential Numbers)
print("\nNumber Right Angle Triangle Pattern (Sequential Numbers):")
rows = 4
num = 1
for i in range(rows):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()

# 3.2. Odd Number Right Angle Triangle Pattern
print("\nOdd Number Right Angle Triangle Pattern:")
rows = 4
odd = 1
for i in range(rows):
    for j in range(i + 1):
        print(odd, end=" ")
        odd += 2
    print()

# 3.3. Same Number Right Angle Triangle Pattern
print("\nSame Number Right Angle Triangle Pattern:")
rows = 6
for i in range(1, rows):
    for j in range(i):
        print(i, end=" ")
    print()

# 3.4. Number Right Angle Triangle Pattern (Aligned Right)
print("\nNumber Right Angle Triangle Pattern (Aligned Right):")
rows = 5
for i in range(rows - 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()

# 3.5. Floyd's Triangle
print("\nFloyd's Triangle:")
rows = 5
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 3.6. Pascal's Triangle
print("\nPascal's Triangle:")
rows = 5
for i in range(rows):
    # Print spaces for alignment
    for j in range(rows - i):
        print(" ", end=" ")
    val = 1
    for j in range(i + 1):
        print(val, end="   ")
        val = val * (i - j) // (j + 1)
    print()

# ===============================
# 4. Additional Patterns
# ===============================

print("\n4. Additional Patterns")

# 4.1. Hollow Square Pattern
print("\nHollow Square Pattern:")
size = 6
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 4.2. Hollow Rectangle Pattern
print("\nHollow Rectangle Pattern:")
height = 5
width = 10
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 4.3. Hollow Pyramid Pattern
print("\nHollow Pyramid Pattern:")
rows = 5
for i in range(rows):
    # Print leading spaces for alignment
    for j in range(rows - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        # Print star only at boundaries or for the bottom row
        if i == rows - 1 or j == 0 or j == 2 * i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 4.4. Hourglass Pattern
print("\nHourglass Pattern:")
rows = 5
# Top half (including middle row)
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)
# Bottom half
for i in range(2, rows + 1):
    print(" " * (rows - i) + "* " * i)
