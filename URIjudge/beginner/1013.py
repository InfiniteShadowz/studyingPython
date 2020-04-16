#Python3

#input splitado
a, b, c = input().split()

#atribuindo variaveis
a = int(a)
b = int(b)
c = int(c)

#processamento
maiorAB = (a+b+abs(a-b))//2
maiorABC = (maiorAB+c+abs(maiorAB-c))//2

#output
print('{} eh o maior'.format(maiorABC))
