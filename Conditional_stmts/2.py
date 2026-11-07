amount = int(input("Enter Amount:"))
if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 10
elif amount >= 1000:
    discount = 5
else:
    discount = 0

discount_amt = amount * discount / 100
final_amt = amount - discount_amt
print("discount:", discount)
print("discount amount:", discount_amt)
print("final amount:", final_amt)