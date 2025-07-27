# Operators in Python

# What are Operators?
'''
Operators are used to perform operations on variables and values.
There are several types of operators in Python:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
'''

# ----------------------------
# 1. Arithmetic Operators
# ----------------------------
'''
Arithmetic operators are used to perform mathematical operations on variables and values.
They include:
1. Addition: +
2. Subtraction: -
3. Multiplication: *
4. Division: /
5. Floor Division: //
6. Modulo: %
7. Exponent: **
'''
# Examples:
a = 15
b = 4

print("Arithmetic Operators:")
print("Addition (a + b):", a + b)           # 15 + 4 = 19
print("Subtraction (a - b):", a - b)        # 15 - 4 = 11
print("Multiplication (a * b):", a * b)     # 15 * 4 = 60
print("Division (a / b):", a / b)           # 15 / 4 = 3.75
print("Floor Division (a // b):", a // b)   # 15 // 4 = 3
print("Modulo (a % b):", a % b)             # 15 % 4 = 3
print("Exponentiation (a ** b):", a ** b)   # 15 ** 4 = 50625

# ----------------------------
# 2. Assignment Operators
# ----------------------------
'''
Assignment operators are used to assign values to variables.
They include:
1. Simple Assignment: =
2. Addition Assignment: +=
3. Subtraction Assignment: -=
4. Multiplication Assignment: *=
5. Division Assignment: /=
6. Floor Division Assignment: //=
7. Modulo Assignment: %=
8. Exponent Assignment: **=
9. Bitwise AND Assignment: &=
10. Bitwise OR Assignment: |=
11. Bitwise XOR Assignment: ^=
12. Bitwise Left Shift Assignment: <<=
13. Bitwise Right Shift Assignment: >>=
(Note: Logical assignment operators like '&=&' do not exist in Python.)
'''
# Examples:
x = 10         # Simple Assignment
print("\nInitial value of x:", x)

x += 5         # x = x + 5
print("After x += 5:", x)

x -= 3         # x = x - 3
print("After x -= 3:", x)

x *= 2         # x = x * 2
print("After x *= 2:", x)

x /= 4         # x = x / 4
print("After x /= 4:", x)

x = 10         # Reset x for floor division example
x //= 3        # x = x // 3
print("After x //= 3:", x)

x = 10         # Reset x for modulo example
x %= 3         # x = x % 3
print("After x %= 3:", x)

x = 2          # Reset x for exponentiation assignment
x **= 3        # x = x ** 3
print("After x **= 3:", x)

# Bitwise Assignment Operators
y = 4          # In binary: 100
print("\nInitial value of y (binary 100):", y)

y &= 3         # y = y & 3, Binary: 100 & 011 = 000 -> 0
print("After y &= 3:", y)

y = 4          # Reset y to 4 (binary: 100)
y |= 3         # y = y | 3, Binary: 100 | 011 = 111 -> 7
print("After y |= 3:", y)

y = 4          # Reset y to 4 (binary: 100)
y ^= 3         # y = y ^ 3, Binary: 100 ^ 011 = 111 -> 7
print("After y ^= 3:", y)

y = 4          # Reset y to 4 (binary: 100)
y <<= 1        # y = y << 1, shifts bits left: 100 becomes 1000 -> 8
print("After y <<= 1:", y)

y = 4          # Reset y to 4 (binary: 100)
y >>= 1        # y = y >> 1, shifts bits right: 100 becomes 010 -> 2
print("After y >>= 1:", y)

# ----------------------------
# 3. Comparison Operators
# ----------------------------
'''
Comparison operators are used to compare values and variables.
They include:
1. Equal to: ==
2. Not equal to: !=
3. Greater than: >
4. Less than: <
5. Greater than or equal to: >=
6. Less than or equal to: <=
'''
# Examples:
p = 10
q = 20

print("\nComparison Operators:")
print("Is p equal to q? (p == q):", p == q)    # False
print("Is p not equal to q? (p != q):", p != q)  # True
print("Is p greater than q? (p > q):", p > q)    # False
print("Is p less than q? (p < q):", p < q)       # True
print("Is p greater than or equal to q? (p >= q):", p >= q)  # False
print("Is p less than or equal to q? (p <= q):", p <= q)     # True

# ----------------------------
# 4. Logical Operators
# ----------------------------
'''
Logical operators are used to perform logical operations on variables and values.
They include:
1. Logical AND: and
2. Logical OR: or
3. Logical NOT: not
'''
# Examples:
a_bool = True
b_bool = False

print("\nLogical Operators:")
print("a_bool and b_bool:", a_bool and b_bool)  # False, one operand is False
print("a_bool or b_bool:", a_bool or b_bool)    # True, one operand is True
print("not a_bool:", not a_bool)                # False, because a_bool is True

# ----------------------------
# 5. Identity Operators
# ----------------------------
'''
Identity operators are used to compare the identity of two objects.
They include:
1. is
2. is not
'''
# Examples:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("\nIdentity Operators:")
print("Does list1 equal list2? (list1 == list2):", list1 == list2)   # True (values are equal)
print("Is list1 the same object as list2? (list1 is list2):", list1 is list2)   # False (different objects)
print("Is list1 the same object as list3? (list1 is list3):", list1 is list3)   # True

# ----------------------------
# 6. Membership Operators
# ----------------------------
'''
Membership operators are used to check if a sequence is present in an object.
They include:
1. in
2. not in
'''
# Examples:
my_string = "Hello, World!"
my_list = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print("'H' in my_string:", 'H' in my_string)       # True
print("'z' not in my_string:", 'z' not in my_string) # True
print("3 in my_list:", 3 in my_list)                # True
print("6 not in my_list:", 6 not in my_list)          # True

# ----------------------------
# 7. Bitwise Operators
# ----------------------------
'''
Bitwise operators are used to perform bit-level operations on integers.
They include:
1. Bitwise AND: &
2. Bitwise OR: |
3. Bitwise XOR: ^
4. Bitwise NOT: ~
5. Bitwise Left Shift: <<
6. Bitwise Right Shift: >>
'''
# Examples:
x = 10      # In binary: 1010
y = 4       # In binary: 0100

print("\nBitwise Operators:")
print("Bitwise AND (x & y):", x & y)   # 1010 & 0100 = 0000 -> 0
print("Bitwise OR (x | y):", x | y)     # 1010 | 0100 = 1110 -> 14
print("Bitwise XOR (x ^ y):", x ^ y)    # 1010 ^ 0100 = 1110 -> 14
print("Bitwise NOT (~x):", ~x)          # Bitwise NOT inverts bits, result in two's complement representation
print("Bitwise Left Shift (x << 1):", x << 1)  # Shifts bits left: 1010 becomes 10100 -> 20
print("Bitwise Right Shift (x >> 1):", x >> 1)  # Shifts bits right: 1010 becomes 0101 -> 5
