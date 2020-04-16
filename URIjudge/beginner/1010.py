#Python3

#split input
a, b, c = input().split()
d, e, f = input().split()

#atribuicao variavel
a = int(a)
b = int(b)
c = float(c)

d = int(d)
e = int(e)
f = float(f)

#processamento
total = b*c + e*f

#output
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
