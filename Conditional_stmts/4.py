units = eval(input("Enter units:"))
rate = int(input("Enter rate:"))
if units<=100:
   rate = 2
elif units <=200:
   rate =3
elif units<=300:
   rate = 5
else:
    rate = 7
bill = units*rate
print("rate per unit", rate)
print(" Total electricity bill", bill)
