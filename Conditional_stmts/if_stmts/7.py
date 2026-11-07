# Write a Python program that determines if a number is a perfect cube

num = int(input("Enter a number: "))

root = round(num ** (1 / 3))

if root * root * root == num:
    print(" number is a perfect cube")
else:
    print("number is not a perfect cube")