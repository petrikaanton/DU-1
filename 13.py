z = int(input("Zadaj číslo:"))
x = 0
if z >= 1:
    for i in range(1,z+1):
        if i % 2 == 0:
            x += i
    print(x)
else:
    print("Číslo musý byť väčšie alebo rovné 1")