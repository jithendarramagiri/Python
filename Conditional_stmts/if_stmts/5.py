# Write a Python program that determines if a given number is a perfect square.
n = int(input("Enter a number: "))
root = int(n**0.5)
if root*root == n:
    print("n is a perfect square")
else:
    print("n is not a perfect square")