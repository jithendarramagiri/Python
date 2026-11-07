order_amt = eval(input("Enter order amount:"))
if order_amt >= 2000:
    delivery_charge = 0
elif order_amt >= 1000:
    delivery_charge = 50
else :
    delivery_charge = 50
final_amt = order_amt+delivery_charge
print("delivery charge", delivery_charge)
print("final amount " , final_amt)

