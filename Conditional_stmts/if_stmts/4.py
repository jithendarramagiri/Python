# 4. Write a Python program that checks if a number is a multiple of both 3 and 5.

n = int(input("Enter a  number:"))
if n%3 == 0 and n%5 == 0:
    print("Multiple of 3 and 5")
else :
    print("Not a multiple of 3 or 5")