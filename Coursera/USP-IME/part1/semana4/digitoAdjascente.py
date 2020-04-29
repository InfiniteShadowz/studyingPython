#Python3

n = int(input())

digAnterior = 0
digAtual = n % 10
n = n // 10
digAdjascente = False

while n != 0:
    digAnterior = n % 10
    n = n // 10
    if digAtual == digAnterior:
        digAdjascente = True
        n = 0
    digAtual= digAnterior
        
if (digAdjascente):
    print("sim")
else:
    print("não")
