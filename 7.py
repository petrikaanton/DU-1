N=int(input("Zadaj číslo:"))
if N<=1:
    print("číslo musí biť väčší alebo rovné 1")
else:
    for i in range(1, N+1):
        if i % 3 == 0:
            print(i)