# Numbers Datatype in Python

# What are Numbers?
"""
Numbers are used to represent numerical values.
They consist of :
1. Integer (int)
2. Floating-point (float)
3. Complex (complex)
"""
# Integer (int)
# It is a whole number, positive or negative or zero
a = 10
print("Integer:", a)
print("Type of a:", type(a))

# Floating-point (float)
# It is a decimal number containing positive or negative decimal nimber
b = 3.14
c = -2.5
print("Floating-point:", b)
print("Floating-point:", c)
print("Type of b:", type(b))
print("Type of c:", type(c))

# Complex (complex)
# It is a combination of real and imaginary parts
# Note: The imaginary part is denoted only by 'j' and not others
d = 2 + 3j
print("Complex:", d)
print("Type of d:", type(d))

# ------------------------------
# Type conversion or type casting
# ------------------------------

# Converting from one type to another
print("\nConverting from one type to another:")
a = float(1)
b = int(3.14)
c = complex(2)
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))