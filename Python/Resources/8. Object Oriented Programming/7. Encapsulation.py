# Encapsulation in Python


# What is Encapsulation?
'''
Encapsulation is one of the fundamental concept in OOPS
It is the idea of wrapping data and methods together inside a capsule (or) class

(Methods | Variables)
        Class

There are two types of encapsulation in Python:

1. Private Method Encapsulation
2. Public Method Encapsulation
'''

# ------------------------------
# Private Method Encapsulation
# ------------------------------

# What is Private Method Encapsulation?
'''
Private method encapsulation is the process of hiding the implementation details of a class from the outside world.
Private methods are not accessible outside the class, and can only be accessed by other methods within the class.
'''

# Example:
class Microsoft:
    def __init__(self):
        self._microsoft365 = "Microsoft 365 Paid Plans"

    def microsoft365(self):
        print("Private Method Encapsulation")
        print(self._microsoft365)

C1 = Microsoft()
C1.microsoft365()


# --------------------------
# Public Method Encapsulation
# --------------------------

# What is Public Method Encapsulation?
'''
Public method encapsulation is the process of hiding the implementation details of a class from the outside world.
Public methods are accessible outside the class, and can be called by other methods or objects outside the class.
'''

# Example:
class Google:
    def __init__(self):
        print("\nPublic Method Encapsulation")
        self.storage = "Google One Paid Access"
        print(self.storage)

C1 = Google()
C1.storage = "Google One Free Access"
print(C1.storage)

