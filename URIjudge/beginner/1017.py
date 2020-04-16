#Python3

#nput
horaGasta = int(input())
velMedia = int(input())

#processamento
desloca = horaGasta * velMedia
litroNecessario = desloca / 12

#Output
print('{:.3f}'.format(litroNecessario))
