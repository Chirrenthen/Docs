# Decision Making Using if Statements in Python

# Decision Making
"""
--- Decision Making ---
  Decision-making statements in Python are used to control the flow of a program based on certain conditions.

1. Simple if Statement
2. if Statement with Logical Operators (and, or, not)
3. if-else Statement
4. if-elif-else Statement
5. Nested if Statement
"""

# -------------------
# Decision Making in Python
# -------------------

# 1. Simple if Statement
num = 10
if num > 5:
    print("if: num is greater than 5")

# 2. if Statement with Logical Operators
# Using 'and': both conditions must be true.
num1, num2 = 5, 10
if num1 < num2 and num2 > num1:
    print("Logical AND: num1 < num2 and num2 > num1")

# Using 'or': at least one condition must be true.
if num1 < num2 or num2 < num1:
    print("Logical OR: At least one condition is True")

# Using 'not': inverts the condition.
if not num1 > num2:
    print("Logical NOT: not(num1 > num2) is True")

# 3. if-else Statement
value = 5
if value > 5:
    print("if-else: value is greater than 5")
else:
    print("if-else: value is not greater than 5")

# 4. if-elif-else Statement
number = 5
if number > 5:
    print("if-elif-else: number is greater than 5")
elif number == 5:
    print("if-elif-else: number is equal to 5")
else:
    print("if-elif-else: number is less than 5")

# 5. Nested if Statement
nested_value = 5
if nested_value > 5:
    print("Nested if: nested_value is greater than 5")
    # Inner if: This block will run only if the outer condition is true.
    if nested_value == 5:
        print("Nested if (inner): nested_value equals 5")
else:
    print("Nested if: nested_value is not greater than 5")
    