# 1. Write a Python program to find and print the first prime number greater than 100.
# Use a loop and the break statement to exit the loop once you find the prime number

# for num in range(101, 200):
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print("First prime number greater than 100:", num)
#         break

# 2. Create a Python program to calculate the sum of all numbers from 1 to 100. However, if the number is divisible by both 3 and 5,
# skip it using the continue statement.

# total = 0
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         continue
#     total = total + num
# print("Sum:", total)

# 3.Write a Python program to find and print the factors of a given number (input by the user).
# Use a loop and the break statement to exit the loop once you find all factors.

# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)
#     if i == num:
#         break

