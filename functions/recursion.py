# w.a.p sum of first ten natural numbers by using recursion

def Natural(n):
    if n ==1:
        return 1
    else:
        return n + Natural(n-1)
n = 10
print(Natural(n))






