# The Odd-Even Challenge Solution
'''

'''

def checknumber(o):
    if o%2 != 0:
        print("Odd Number")
    elif 0 < o < 40:
        print("Even number between 0 and 40")
    elif 40 < o < 60:
        print("Even number between 40 and 60")
    elif o > 60:
        print("Even number greater than 60")
    else:
        print("Invalid")

a=int(input("Enter a number: "))

t = 0
for i in range(a):
    s=i*i
    t+=s

checknumber(t)