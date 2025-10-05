limit=int(input("zadaj horný limit:"))
if limit<5:
    print("limit musí biť väčší ako 1")
else:
    for i in range(5,limit+1):
        if (i//2)!=(i/2):
            print(i)
        else:
            print()
