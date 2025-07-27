import cmath
import math

a = 1
b = 5
c = 1

d = (b**2) - (4*a*c)

print(f"Quadratic equation: {a}x^2 + {b}x + {c} = 0")
print(f"Discriminant (D): {d}")

if d > 0:
    # Real and distinct roots
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots are real and distinct.")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif d == 0:
    # Real and equal roots
    root = -b / (2*a)
    print(f"Roots are real and equal.")
    print(f"Root: {root}")
else:
    # Complex roots
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    print(f"Roots are complex.")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")