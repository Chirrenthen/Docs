# String Datatype in Python

# What is a String?
"""
A string is a sequence of characters.
It is stored between single quotes or double quotes.
It is immutable, which means you cannot change it after it's created.
"""

# ------------------------------
# Creating Strings
# ------------------------------

str1 = 'Hello'            # String with single quotes
str2 = "I'm Python"       # String with double quotes

# ------------------------------
# Printing Strings
# ------------------------------

print("String 1:", str1)
print("String 2:", str2)

# ------------------------------
# Checking Type and Length
# ------------------------------

print("\nChecking Type of String:")
print("Type of str1:", type(str1))
print("Type of str2:", type(str2))

print("\nChecking Length of String:")
print("Length of str1:", len(str1))
print("Length of str2:", len(str2))

# ------------------------------
# Looping through Strings
# ------------------------------

print("\nLooping through a String (character by character):")
str3 = "Python"
for char in str3:
    print(char)

# -------------------------------
# Accessing Characters in a String
# -------------------------------

print("\nAccessing characters by index:")
print("First character of str1 (str1[0]):", str1[0])
print("Characters from index 2 to 4 in str2 (str2[2:5]):", str2[2:5])

print("\nSlicing a string:")
print("Characters from index 2 to end in str1 (str1[2:]):", str1[2:])
print("First five characters of str2 (str2[:5]):", str2[:5])

# ------------------------------
# String Concatenation and Repetition
# ------------------------------

print("\nString Concatenation:")
str4 = "Python"
str5 = "Development"
str6 = "Innovation"
str7 = str4 + " + " + str5 + " = " + str6
print("Concatenated string:", str7)

print("\nString Repetition:")
str8 = "Python"
str9 = str8 * 3
print("Repeated string:", str9)

# ------------------------------
# String Formatting
# ------------------------------

print("\nString Formatting (old style):")
str10 = "Python"
str11 = "Development"
str12 = "Innovation"
str13 = "%s + %s = %s" % (str10, str11, str12)
print("Formatted string:", str13)

# ------------------------------
# String Methods (Manipulating Strings)
# ------------------------------

# 1. upper() -> Returns the string in uppercase
print("\nupper() method:")
str14 = "python"
str15 = str14.upper()
print("Uppercase string:", str15)

# 2. lower() -> Returns the string in lowercase
print("\nlower() method:")
str16 = "PYTHON"
str17 = str16.lower()
print("Lowercase string:", str17)

# 3. capitalize() -> Capitalizes the first character of the string
print("\ncapitalize() method:")
str18 = "python"
str19 = str18.capitalize()
print("Capitalized string:", str19)

# 4. strip() -> Removes leading and trailing spaces
print("\nstrip() method:")
str20 = "   Python   "
str21 = str20.strip()
print("Stripped string:", str21)

# 5. lstrip() -> Removes spaces from the left
print("\nlstrip() method:")
str22 = "   Python   "
str23 = str22.lstrip()
print("Left stripped string:", str23)

# 6. rstrip() -> Removes spaces from the right
print("\nrstrip() method:")
str24 = "   Python   "
str25 = str24.rstrip()
print("Right stripped string:", str25)

# 7. replace() -> Replaces specified characters or substring
print("\nreplace() method:")
str26 = "Python"
str27 = str26.replace("P", "p")
print("Replaced string:", str27)

# 8. split() -> Splits the string into a list using a separator
print("\nsplit() method:")
str28 = "Python, Development, Innovation"
str29 = str28.split(", ")
print("Split string:", str29)

# 9. format() -> Formats strings using placeholders
print("\nformat() method:")
str30 = "Python"
str31 = "Development"
str32 = "Innovation"
str33 = "{} + {} = {}"
str34 = str33.format(str30, str31, str32)
print("Formatted string:", str34)

# 10. find() -> Returns the index of the first occurrence of a substring
print("\nfind() method:")
str35 = "Python"
str36 = str35.find("o")
print("Index of 'o':", str36)

# 11. rfind() -> Returns the index of the last occurrence of a substring
print("\nrfind() method:")
str37 = "Python"
str38 = str37.rfind("o")
print("Index of last 'o':", str38)

# 12. index() -> Returns the index of a substring (error if not found)
print("\nindex() method:")
str39 = "Python"
str40 = str39.index("t")
print("Index of 't':", str40)

# 13. isalnum() -> Returns True if all characters are alphanumeric
print("\nisalnum() method:")
str41 = "Python13"
str42 = str41.isalnum()
print("Is alphanumeric:", str42)

# 14. isalpha() -> Returns True if all characters are alphabetic
print("\nisalpha() method:")
str43 = "GuidoVanRossum"
str44 = str43.isalpha()
print("Is alphabetical:", str44)

# 15. isdigit() -> Returns True if all characters are digits
print("\nisdigit() method:")
str45 = "1234567890"
str46 = str45.isdigit()
print("Is digits:", str46)

# 16. isupper() -> Returns True if all characters are uppercase
print("\nisupper() method:")
str47 = "THIS IS UPPERCASE"
str48 = str47.isupper()
print("Is uppercase:", str48)

# 17. islower() -> Returns True if all characters are lowercase
print("\nislower() method:")
str49 = "this is lowercase"
str50 = str49.islower()
print("Is lowercase:", str50)

# 18. isspace() -> Returns True if all characters are spaces
print("\nisspace() method:")
str51 = "   "
str52 = str51.isspace()
print("Is space:", str52)
