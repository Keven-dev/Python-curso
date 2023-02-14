opção = maior = menor = 0
while opção != 5:
    valor1 = int(input('Digite um valor inteiro: '))
    valor2 = int(input('Digite outro valor inteiro: '))
    print('[1] SOMAR \n[2] MULTIPLICAÇÃO \n[3] MAIOR E MENOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA')
    opção = int(input('Digite a operações acima desejada: '))
    if opção == 1:
        print('A soma entre {} e {} = {}'.format(valor1, valor2, valor1 + valor2))
    elif opção == 2:
        print('A multiplicaçao entre {} e {} = {}'.format(valor1, valor2, valor1 * valor2)) 
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
            menor = valor2
        else:
            maior = valor2
            menor = valor1
        print(f'{maior} é o maior e {menor} é o menor')
    elif opção == 4:
        pass
    elif opção == 5:
        print('=== FIM DO PROGRAMA ===')
        pass
    else:
        print(f'Opção {opção} inexistente, tente novamente')
