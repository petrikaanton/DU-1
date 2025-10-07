z = int(input("Zadaj číslo:"))
x = 0
if z >= 1:
    for i in range(0,z+2):
        x=z-i
        if x >= 1:
            print(x)
else:
    print("Číslo musý byť väčšie alebo rovné 1")