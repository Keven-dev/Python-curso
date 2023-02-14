n = média = maior = menor = qtd_números = soma = 0
opção = ''
while opção != 'N':
    n = int(input('Digite um número inteiro: '))
    soma += n
    qtd_números += 1
    média = soma / qtd_números
    if qtd_números == 1:
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    opção = str(input('Deseja continuar? [S / N]: ')).upper()
    print(' ')
print(f'Números digitados: {qtd_números}')
print(f'Soma: {soma}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Média: {média}')
