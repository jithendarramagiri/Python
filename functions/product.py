def product(n):
    if n == 0:
        return 1
    return (n % 10) * product(n // 10)
n = int(input("Enter any Number :"))
print(product(n))