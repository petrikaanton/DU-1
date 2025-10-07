z = int(input("Zadaj číslo:"))
if z >= 1:
    for i in range(1,z+1):
        if i % 4 == 0 and i % 7 == 0:
            print(i)
else:
    print("Číslo musý byť väčšie alebo rovné 1")