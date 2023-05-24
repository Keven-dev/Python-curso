lista = []
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))
print(f'O menor número foi {min(lista)} na posição ', end= '')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ', end='')
print(' ')

print(f'O maior número foi {max(lista)} na posição ', end='')
for i, v in enumerate(lista): # enumerate i = chave e v = valor
    if v == max(lista):
        print(f'{i}... ', end='')
print(' ')
print(f'Números digitados: {lista}')

