# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)
print()

# 2. Print even numbers from 1 to 20
for i in range(2, 21):
    i+=2
    print(i)
print()

# 3. Sum of the first 10 natural numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum:", sum)
print()

# 4. Multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# 5. Factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)
print()

# 6. Reverse a string
s = input("Enter a string: ")
rev = ""
for char in s:
    rev = char + rev
print("Reversed String:", rev)
print()

# 7. Count vowels in a string
s = input("Enter a string: ")
count = 0
for char in s.lower():
    if char in "aeiou":
        count += 1
print("Vowel Count:", count)
print()

# 8. Find the largest element in a list
lst = [3, 7, 1, 9, 4]
largest = lst[0]
for num in lst:
    if num > largest:
        largest = num
print("Largest Element:", largest)
print()

# 9. Sum of all elements in a list
sum = 0
for num in lst:
    sum += num
print("Sum of List Elements:", sum)
print()

# 10. Print list elements in reverse order
for i in range(len(lst) - 1, -1, -1):
    print(lst[i])
print()

# 11. Check if a number is prime
num = int(input("Enter a number: "))
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
        break
print("Prime" if prime and num > 1 else "Not Prime")
print()

# 12. Print Fibonacci numbers up to n
n = int(input("Enter n: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# 13. Find GCD of two numbers
a, b = map(int, input("Enter two numbers: ").split())
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print("GCD:", i)
        break
print()

# 14. Print Armstrong numbers from 1 to 1000
for num in range(1, 1001):
    sum = 0
    temp = num
    for digit in str(num):
        sum += int(digit) ** len(str(num))
    if sum == num:
        print(num)
print()

# 15. Check if a number is a palindrome
num = input("Enter a number: ")
print("Palindrome" if num == num[::-1] else "Not Palindrome")
