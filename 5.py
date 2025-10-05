a=int(input("Zadaj 1. číslo:"))
b=int(input("Zadaj 2. číslo:"))
if a<b:
    for i in range(a,b+1):
        print(i, round(i**(1/2),2))
else:
    for i in range(b,a+1):
        print(i, round(i ** (1 / 2), 2))