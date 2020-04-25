#Python3

n = int(input())
n += 0.001

nota100 = n // 100
n = n % 100
nota50 = n // 50
n = n % 50
nota20 = n // 20
n = n % 20
nota10 = n // 10
n = n % 10
nota5 = n // 5
n = n % 5
nota2 = n // 2
n = n % 2


moeda1 = n // 1
n = n % 1
moeda5 = n // 0.5
n = n % 0.5
moeda25 = n // 0.25
n = n % 0.25
moeda10 = n // 0.1
n = n % 0.1
moeda5 = n // 0.05
n = n % 0.05
moeda01 = valor // 0.01

#prints


print("NOTAS:")
print(nota100, "nota(s) de R$ 100.00")
print(nota50, "nota(s) de R$ 50.00")
print(nota20, "nota(s) de R$ 20.00")
print(nota10, "nota(s) de R$ 10.00")
print(nota5, "nota(s) de R$ 5.00")
print(nota2, "nota(s) de R$ 2.00")

print("MOEDAS:")
print(moeda1, "moeda(s) de R$ 1.00")
print(moeda5, "moeda(s) de R$ 0.50")
print(moeda25, "moeda(s) de R$ 0.25")
print(moeda10, "moeda(s) de R$ 0.10")
print(moeda5, "moeda(s) de R$ 0.05")
print(moeda01, "moeda(s) de R$ 0.01")

