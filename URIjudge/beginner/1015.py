#Python3

#input
x, y = input().split()
x1, y1 = input().split()

#atribuindo variaveis
x = float(x)
y = float(y)
x1 = float(x1)
y1 = float(y1)

#processamento
dist = (((x1-x)**2)+((y1-y)**2))**0.5

#Output format
print('{:.4f}'.format(dist))
