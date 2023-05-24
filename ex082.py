lista = []
lista_impar = []
lista_par = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continua = str(input('Deseja continuar? [S/N]')).upper()
    if continua == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
    
print(f'Lista completa {lista}')
print(f'Lista com números pares {lista_par}')
print(f'Lista com números impar {lista_impar}')
