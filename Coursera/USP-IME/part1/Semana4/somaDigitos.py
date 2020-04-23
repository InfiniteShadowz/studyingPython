#Python3

n = int(input("Digite um numero inteiro: "))

soma = 0

while n != 0:
    soma += n % 10
    n = n // 10

print(soma)
    


