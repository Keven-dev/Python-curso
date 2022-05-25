from math import pow, sqrt
co = float(input('Digite o valor do cateto oposto ao ângulo: '))
ca = float(input('Digite o valor do cateto adjacente ao ângulo: '))
co = pow(co, 2)
ca = pow(ca, 2)
soma = co + ca
h = sqrt(soma)
print('O comprimento da hipotenusa igual a {:.0f}'.format(h))
