#Python3

num = int(input("Digite um número: "))
lista = []
while num != 0:
    lista.append(num)
    num = int(input("Digite um número: "))
    

lista.reverse()

for i in lista:
    print(i)
