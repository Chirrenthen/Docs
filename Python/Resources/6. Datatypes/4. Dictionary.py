# Dictionary Datatype in Python

# What is a Dictionary?
"""
Dictionaries are used to store data in key-value pairs.
They are mutable, meaning their values can be changed after creation.
Dictionaries use curly braces {} for definition.
They don't allow duplicate keys.
"""

# Creating Dictionaries
dict1 = {"name": "Python", "age": 33, "city": "Netherlands"}  # Dictionary with strings as keys
dict2 = {1: "apple", 2: "banana", 3: "cherry"}  # Dictionary with integers as keys

# Printing Dictionaries
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

# ------------------------------
# Checking Type and Length of a Dictionary
# ------------------------------

# Checking the type of a dictionary
print("\nChecking Type of Dictionary:")
print("Type of dict1:", type(dict1))
print("Type of dict2:", type(dict2))

# Checking the length of a dictionary
print("\nChecking Length of Dictionary:")
print("Length of dict1:", len(dict1))
print("Length of dict2:", len(dict2))

# ------------------------------
# Accessing Dictionary Elements
# ------------------------------

# Accessing elements by key
print("\nAccessing Dictionary Elements:")
print("Name:", dict1["name"])
print("Age:", dict1["age"])
print("City:", dict1["city"])

# Dictionary Constructor
print("\nDictionary Constructor:")
dict3 = dict(name="Python", age=33, city="Netherlands")
print("Dictionary 3:", dict3)

# ------------------------------
# Loops in Dictionaries
# ------------------------------

# Looping through key-value pairs
print("\nLooping through a Dictionary (key-value pairs):")
for key, value in dict1.items():
    print(key, ":", value)

# Looping through keys
print("\nLooping through a Dictionary (keys):")
for key in dict1.keys():
    print(key)

# Looping through values
print("\nLooping through a Dictionary (values):")
for value in dict1.values():
    print(value)

# ------------------------------
# Dictionary Methods (Manipulating Dictionaries)
# ------------------------------

# 1. update() → Updates the dictionary with the specified key-value pairs
print("\nupdate() method:")
dict1.update({"age": 34})
print("Updated dict1:", dict1)

# 2. clear() → Removes all elements from the dictionary
print("\nclear() method:")
dict2.clear()
print("Cleared dict2:", dict2)

# 3. pop() → Removes the element with the specified key 
print("\npop() method:")
dict1.pop("name")
print("After popping 'name' from dict1:", dict1)

# 4. popitem() → Removes the last inserted key-value pair
print("\npopitem() method:")
dict1.popitem()
print("After popitem on dict1:", dict1)

# 5. copy() → Returns a shallow copy of the dictionary
print("\ncopy() method:")
dict4 = dict1.copy()
print("Copied dict4:", dict4)

# 6. get() → Returns the value of the specified key
print("\nget() method:")
print("Value of 'name' key:", dict1.get("name"))

# 7. keys() → Returns a list of all the keys in the dictionary
print("\nkeys() method:")
print("Keys in dict1:", list(dict1.keys()))

# 8. values() → Returns a list of all the values in the dictionary
print("\nvalues() method:")
print("Values in dict1:", list(dict1.values()))

# 9. items() → Returns a list of all the key-value pairs in the dictionary
print("\nitems() method:")
print("Items in dict1:", list(dict1.items()))

# 10. setdefault() → Returns the value of the specified key (and sets it if not present)
print("\nsetdefault() method:")
print("Value of 'name' key:", dict1.setdefault("name", "Default Value"))
