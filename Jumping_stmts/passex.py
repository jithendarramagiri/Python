# 1. Create a Python program that iterates over a list of integers and prints all even numbers.
# For odd numbers, use the pass statement to do nothing.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#     else:
#         pass

# 2.Write a Python program that asks the user to input a list of numbers. For each number in the list, check if it's a prime number.
# If it's prime, print it; if not, use the pass statement.

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11]
for num in numbers:
    prime = True
    if num < 2:
        prime = False
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
    else:
        pass

# Implement a Python  program that simulates  a basic class structure for a geometric shape.
# # Create a class named Shape, and for now, use the pass statement to indicate that further methods need to be added in the future.
#
# class Shape:
#     pass
# shape = Shape()
# print("Shape object created")
