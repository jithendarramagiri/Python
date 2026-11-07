# Write a Python program that checks if a number is divisible by both 2 and 3.
n = int(input("Enter a number:"))
if n%2 == 0 and n%3==0:
    print("n is divisible by 2 and 3")
else:
     print("n is not divisible by 2 and 3")