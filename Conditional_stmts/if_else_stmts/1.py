# Write a Python program that checks if a given year is a leap year.
n = int(input("Enter any year:"))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("leap year")
else :
    print("not leap year")