lista = [] 
n_digitados = 0
msg_5 = ''
while True:
    n = int(input('Digite um valor: ')) 
    lista.append(n)
    n_digitados += 1
    

    if n == 5:
        msg_5 = 'O valor 5 foi digitado'
    else:
        msg_5 = 'O valor 5 não foi digitado'

    continua = str(input('Deseja continuar? [S/N]')).upper()
    if continua == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {n_digitados} Números')
print(f'Lista de forma decrescente {lista}')
print(f'{msg_5}')

