# Decision Making using Loop Statements in Python

# Loops
'''
--- Loops ---
 Loops in Python are used to repeat a block of code multiple times based on certain conditions.

1. Basic for Loop using range()
2. For Loop with break, continue, and else
3. Nested for Loops
4. Basic while Loop
5. While Loop with break, continue, and else
'''
# -------------------
#      Loops
# -------------------

# 1. Basic for Loop using range()
print("\nBasic for loop using range():")
for i in range(1, 11):  # Generates numbers from 1 to 10
    print("For loop (range): Number", i)

# 2. For Loop with break, continue, and else
print("\nFor loop with break, continue, and else:")
for i in range(1, 11):
    if i == 5:
        print("For loop: Skipping number 5 using continue")
        continue  # Skip the current iteration when i equals 5
    if i == 8:
        print("For loop: Breaking out of the loop at 8")
        break    # Exit the loop when i equals 8
    print("For loop (control): Number", i)
else:
    # The else clause executes only if the loop completes normally (no break encountered).
    print("For loop: Completed without break")

# 3. Nested for Loops
print("\nNested for loops example:")
for row in range(1, 4):  # Outer loop: rows 1 to 3
    print("Row", row)
    for col in range(1, 4):  # Inner loop: columns 1 to 3
        print("   Column", col)

# 4. Basic while Loop
print("\nBasic while loop example:")
counter = 1
while counter <= 5:
    print("While loop (basic): Counter", counter)
    counter += 1  # Increment counter to eventually exit the loop

# 5. While Loop with break, continue, and else
print("\nWhile loop with break, continue, and else:")
counter = 1
while counter <= 10:
    if counter == 3:
        print("While loop: Counter is 3; using continue to skip iteration")
        counter += 1  # Increment before continue to avoid infinite loop
        continue     # Skip the rest of the current iteration
    if counter == 7:
        print("While loop: Counter reached 7; breaking out of the loop")
        break        # Exit the loop when counter equals 7
    print("While loop (control): Counter", counter)
    counter += 1
else:
    # Executes only if the loop condition becomes false without encountering a break.
    print("While loop: Completed without break")

