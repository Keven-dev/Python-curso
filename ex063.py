número = int(input('Digite um número qualquer: '))
elementos = 0
soma = 0
parcela1 = 0
parcela2 = 1
while elementos < número:
    print(f'{soma}, ')
    parcela1 = parcela2
    parcela2 = soma
    soma = parcela1 + parcela2
    elementos += 1
print('FIM')
