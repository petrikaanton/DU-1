z = int(input("zadaj z:"))
k = int(input("zadaj k:"))
x = 0
if z <= k:
    for i in range(z,k+1):
         if i % 2 == 0:
             x += i
    print(x)
else:
    for i in range(k,z+1):
        if i % 2 == 0:
            x += i
    print(x)