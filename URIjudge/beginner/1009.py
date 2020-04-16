#Python3

#input
nome = input()
salarioFixo = float(input())
totalVendas = float(input())

#processamento
total = salarioFixo + totalVendas*0.15

#output formatado 2casas
print("TOTAL = {:.2f}".format(total))
