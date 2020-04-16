#Python3


#input split
A, B, C = input().split()

#atribuindo variaveis
A = float(A)
B = float(B)
C = float(C)

#area do triangulo
a = (A*C)/2
#area do circulo
b = 3.14159*C**2
#area do trapezio:
c = ((A+B)*C)/2
#area do quadrado
d = B*B
#area do retangulo
e = A*B

#output
print('TRIANGULO: {:.3f}'.format(a))
print('CIRCULO: {:.3f}'.format(b))
print('TRAPEZIO: {:.3f}'.format(c))
print('QUADRADO: {:.3f}'.format(d))
print('RETANGULO: {:.3f}'.format(e))
