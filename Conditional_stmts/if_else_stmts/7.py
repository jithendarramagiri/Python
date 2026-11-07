# # Write a Python program that compares two numbers and prints the larger one.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1>num2:
#     print("Larger number is:", num1)
# else:
#     print("Larger number is:", num2)



l = [26, 17, 19, 18, 7, 23]
target = 100

for i in range(len(l)):
     if l[i] == target:
        print(f"Target element {target} found at position {i}")
        break
else :
    print("Target element not found")