# Sets Datatype in Python

# What is a Set?
"""
Sets are used to store multiple items in a single variable.
They are unordered, meaning the order of elements is not guaranteed.
Sets use curly braces {} for definition.
Sets don't allow duplicate elements.
"""

# Creating Sets
set1 = {1, 2, 3, 4, 5}             # Set with integers
set2 = {"apple", "banana", "cherry"} # Set with strings

# Printing Sets
print("Set 1:", set1)
print("Set 2:", set2)

# ------------------------------
# Checking Type and Length of a Set
# ------------------------------

print("\nChecking Type of Set:")
print("Type of set1:", type(set1))
print("Type of set2:", type(set2))

print("\nChecking Length of Set:")
print("Length of set1:", len(set1))
print("Length of set2:", len(set2))

# ------------------------------
# Set Constructor
# ------------------------------

print("\nSet Constructor:")
set3 = set([1, 2, 3, 4, 5])
print("Set 3:", set3)

# ------------------------------
# Looping through a Set
# ------------------------------

print("\nLooping through a Set:")
for x in set1:
    print(x)

# ------------------------------
# Set Methods (Manipulating Sets)
# ------------------------------

# 1. add() → Adds an element to the set
print("\nadd() method:")
set1.add(6)
print("Updated set1:", set1)

# 2. remove() → Removes an element from the set
print("\nremove() method:")
set1.remove(6)
print("Updated set1:", set1)

# 3. update() → Adds elements from another set to the current set
print("\nupdate() method:")
set1.update([7, 8, 9])
print("Updated set1:", set1)

# 4. pop() → Removes and returns an arbitrary element from the set
print("\npop() method:")
set1.pop()
print("Updated set1:", set1)

# 5. clear() → Removes all elements from the set
print("\nclear() method:")
set1.clear()
print("Cleared set1:", set1)

# 6. discard() → Removes the specified element from the set if present
print("\ndiscard() method:")
# Note: set1 is empty now due to clear(), so we'll add elements back for demonstration.
set1 = {1, 2, 3, 4, 5}
set1.discard(4)
print("Updated set1 after discarding 4:", set1)

# 7. union() → Returns a new set with all elements from both sets
print("\nunion() method:")
set4 = {10, 11, 12}
set5 = set1.union(set4)
print("Union of set1 and set4:", set5)

# 8. intersection() → Returns a new set with elements common to both sets
print("\nintersection() method:")
set6 = set1.intersection(set4)
print("Intersection of set1 and set4:", set6)

# 9. difference() → Returns a new set with elements in set1 but not in set4
print("\ndifference() method:")
set7 = set1.difference(set4)
print("Difference of set1 and set4:", set7)

# 10. symmetric_difference() → Returns a new set with elements in either set1 or set4 but not in both
print("\nsymmetric_difference() method:")
set8 = set1.symmetric_difference(set4)
print("Symmetric difference of set1 and set4:", set8)

# 11. issubset() → Returns True if one set is a subset of another
print("\nissubset() method:")
set9 = {1, 2, 3}
set10 = {1, 2, 3, 4, 5}
print("Is set9 a subset of set10?", set9.issubset(set10))

# 12. issuperset() → Returns True if one set is a superset of another
print("\nissuperset() method:")
print("Is set10 a superset of set9?", set10.issuperset(set9))

# 13. isdisjoint() → Returns True if two sets have no elements in common
print("\nisdisjoint() method:")
print("Are set9 and set10 disjoint?", set9.isdisjoint(set10))
