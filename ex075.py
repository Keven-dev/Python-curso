v = (int(input('Digite um número: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite mais um valor: ')),
    int(input('Digite o último valor: ')))
tupla = (v)
print(tupla)
if 9 in tupla:
    print(f'O número 9 apareceu {tupla.count(9)} vez(es)')
else:
    print('O valor 9 não foi digitado, portanto não apareceu.')
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado.')

print(f'Os número pares digitados foram ', end='')
par = 0
for n in tupla:
    if n % 2 == 0:
      print(n, end=' ')
      par += 1    
if par == 0:
    print('Nenhum.')
    
