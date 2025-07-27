# List Dataype in Python

# What is a List? 
'''
A list is a collection that:
 Stores multiple items in a single variable.
 Is ordered (elements have a fixed position).
 Is changeable (mutable).
 Allows duplicate values.
 Uses square brackets [] for definition.
 Works with indexes (0 to n-1).
'''

# Creating Lists
list1 = [1, 2, 3, 4, 5]  # List with integers
list2 = ["apple", "banana", "cherry"]  # List with strings
list3 = [1, "orange", True, 3.14, "watermelon"]  # List with mixed data types

# Printing Lists
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)

# ------------------------------
# Checking Type and Length of a List
# ------------------------------

# Checking the type of a list
print("\nChecking Type of List:")
print("Type of list1:", type(list1))
print("Type of list2:", type(list2))
print("Type of list3:", type(list3))

# Checking the length (number of elements in a list)
print("\nChecking Length of List:")
print("Length of list1:", len(list1))
print("Length of list2:", len(list2))
print("Length of list3:", len(list3))

# ------------------------------
# Accessing Elements in a List
# ------------------------------

print("\nAccessing Elements of a List:")

# Accessing elements using positive indexing (starts from 0)
print("Element at index 2 in list1:", list1[2])  # Output: 3

# Accessing elements using negative indexing (starts from -1)
print("Last element in list1:", list1[-1])  # Output: 5

# Slicing (getting a subset of elements)
print("Elements from index 2 to end:", list1[2:])  # Output: [3, 4, 5]
print("Elements from index 1 onwards:", list1[1:])  # Output: [2, 3, 4, 5]
print("Elements before index 2:", list1[:2])  # Output: [1, 2]

# ------------------------------
# Creating a List Using Constructor
# ------------------------------

print("\nCreating a List Using list() Constructor:")
list4 = list(("apple", "banana", "cherry"))  # Double parentheses required
print("List created with constructor:", list4)

# ------------------------------
# List Methods (Manipulating Lists)
# ------------------------------

# 1. append() → Adds an element at the end
print("\nappend() method:")
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# 2. insert() → Inserts an element at a specific position
print("\ninsert() method:")
my_list.insert(2, 99)
print(my_list)  # Output: [1, 2, 99, 3, 4]

# 3. remove() → Removes the first occurrence of a specific value
print("\nremove() method:")
my_list.remove(99)
print(my_list)  # Output: [1, 2, 3, 4]

# 4. extend() → Merges another list into the current list
print("\nextend() method:")
listA = [1, 2, 3]
listB = [4, 5, 6]
listA.extend(listB)
print(listA)  # Output: [1, 2, 3, 4, 5, 6]

# 5. clear() → Removes all elements from a list
print("\nclear() method:")
listA.clear()
print(listA)  # Output: []

# 6. copy() → Returns a shallow copy of the list
print("\ncopy() method:")
listC = [1, 2, 3]
listD = listC.copy()
print(listD)  # Output: [1, 2, 3]

# 7. pop() → Removes and returns the last element (or specified index)
print("\npop() method:")
listC.pop()
print(listC)  # Output: [1, 2]

# 8. sort() → Sorts the list in ascending order
print("\nsort() method:")
listE = [3, 1, 2]
listE.sort()
print(listE)  # Output: [1, 2, 3]

# Sorting in descending order
listE.sort(reverse=True)
print(listE)  # Output: [3, 2, 1]

# 9. reverse() → Reverses the list order
print("\nreverse() method:")
listF = [1, 2, 3]
listF.reverse()
print(listF)  # Output: [3, 2, 1]

# 10. count() → Counts occurrences of a value
print("\ncount() method:")
listG = [1, 2, 3, 3, 4, 5]
print("Count of 3:", listG.count(3))  # Output: 2

# 11. index() → Finds the first occurrence of a value
print("\nindex() method:")
print("Index of 3:", listG.index(3))  # Output: 2

# 12. min() → Returns the smallest element
print("\nmin() method:")
listH = [10, 20, 5, 40]
print("Minimum value:", min(listH))  # Output: 5

# 13. max() → Returns the largest element
print("\nmax() method:")
print("Maximum value:", max(listH))  # Output: 40

# 14. sum() → Returns the sum of all elements
print("\nsum() method:")
print("Sum of list elements:", sum(listH))  # Output: 75

# ------------------------------
# Additional List Features
# ------------------------------

# List comprehension (creating a new list with conditions)
print("\nList Comprehension Example:")
squared_numbers = [x**2 for x in range(5)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16]

# Checking if an element exists in a list
print("\nChecking if an element exists in a list:")
my_list = ["apple", "banana", "cherry"]
if "banana" in my_list:
    print("Yes, 'banana' is in the list.")  # Output: Yes, 'banana' is in the list.

# Iterating through a list
print("\nIterating through a list:")
for item in my_list:
    print(item)
