a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b*b - 4*a*c

if delta > 0:
    x1 = (-b + delta**1/2) / (2*a)
    x2 = (-b - delta**1/2) / (2*a)
    print("x1 =",x1,"\nX2 =",x2)
elif delta == 0:
    x1 = -b / (2*a)
    x2 = x1
    print("x1 =",x1,"\nX2 =",x2)
else:
    print("Não existem raízes reais!")
