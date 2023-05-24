valores = []
resp = 'S'
valor = 0
while resp == 'S':
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('erro, valor duplicado.')
    else:
        valores.append(valor)
    resp = str(input('Deseja continua? [S/N]: ')).upper()
print(f'Os valores digitados foram: {sorted(valores)}')