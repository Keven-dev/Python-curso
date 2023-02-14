numero = int(input('Digite um número inteiro: '))
print(' ')
print('0 - Binário')
print('1 - Octal')
print('2 - Hexadecimal')
print('Escolha base de conversão 0 / 1 / 2 ?')
opcao = int(input('Digite opção: '))
lista_opcao = [0, 1, 2]

if opcao in lista_opcao:
    print('continue o processo...')
else:
    print('Opção inválida!')
