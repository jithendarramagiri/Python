#3. Write a Python program that determines if a number is positive, negative, or zero using only if statements and no elif or else.

n = int(input("Enter a number: "))
if n > 0:
    print("number is positive")
if n < 0:
    print("number is negative")
if n == 0:
    print("number is zero")