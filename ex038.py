print('Escreva dois valores inteiros')
valor1 = int(input('Digite primeiro valor: '))
valor2 = int(input('Digite segundo valor: '))

if valor1 > valor2:
    print(f'O primeiro valor é maior que o segundo | {valor1} é maior que {valor2}')
elif valor2 > valor1:
    print(f'O segundo valor é maior que o primeiro | {valor2} é maior que {valor1}')
else:
    print(f'Os dois valores são iguais | {valor1} é igual a {valor2} ')
