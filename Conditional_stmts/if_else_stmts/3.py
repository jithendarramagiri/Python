# Write a Python program that checks if a given year is a century year (ending in '00')
year = int(input("Enter a year :"))
if year % 100 == 0:
    print("It is a century year")
else:
    print("It is not a century year")