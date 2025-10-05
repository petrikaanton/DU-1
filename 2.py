limit=int(input("zadaj horný limit:"))
if limit<1:
    print("limit musí biť väčší ako 1")
else:
    for i in range(1,limit+1):
        print("a:",i)
    for i in range(1,limit+1):
        if i==1:
            print("b:",i,end=",")
        elif i!=limit:
            print(" b:",i,end=",")
        else:
            print(" b:",i)