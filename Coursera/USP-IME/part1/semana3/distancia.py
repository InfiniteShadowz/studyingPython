#Python3


xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())


dist = ((xa - xb)**2 + (ya - yb)**2)**(1/2)

if dist >= 10:
    print("longe")
else:
    print("perto")



