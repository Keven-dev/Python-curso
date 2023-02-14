from random import choice
from time import sleep 

print('='*20,' JOKENPÔ ','='*20)
print('\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n')
opcao_escolida = int(input('ESCOLHA:(1, 2 OU 3): '))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
opcao_comp = choice(lista)
print('JO!!')
sleep(0.5)
print('KEN!!')
sleep(0.5)
print('PÔ!!\n')
sleep(0.5)

if opcao_escolida == 1 and opcao_comp == 'PEDRA':
    print('Computador escolheu', opcao_comp)
    print('\nVocê e o computador escolheram PEDRA, EMPATE!')
elif opcao_escolida == 2 and opcao_comp == 'PEPEL':
    print('\nComputador escolheu', opcao_comp)
    print('Você e o computador escolheram PAPEL, EMPATE!')
elif opcao_escolida == 3 and opcao_comp == 'TESOURA':
    print('\nComputador escolheu', opcao_comp)
    print('Você e o computador escolheram TESOURA, EMPATE!')
elif opcao_escolida == 1 and opcao_comp == 'PAPEL':
    print('\nComputador escolheu', opcao_comp)
    print('Você escolheu PEDRA e o computador escolheu PAPEL, Computador GANHOU!')
elif opcao_escolida == 1 and opcao_comp == 'TESOURA':
    print('\nComputador escolheu', opcao_comp)
    print('Você escolheu PEDRA e o computador escolheu TESOURA, Você GANHOU!')
elif opcao_escolida == 2 and opcao_comp == 'PEDRA':
    print('\nComputador escolheu', opcao_comp)
    print('Você escolheu PAPEL e o computador escolheu PEDRA, Você GANHOU!')
elif opcao_escolida == 2 and opcao_comp == 'TESOURA':
    print('\nComputador escolheu', opcao_comp)
    print('Você escolheu PAPEL e o computador escolheu TESOURA, Computador GANHOU!')
elif opcao_escolida == 3 and opcao_comp == 'PEDRA':
    print('\nComputador escolheu', opcao_comp)
    print('Você escolheu TESOURA e o computador escolheu PEDRA, Computador GANHOU!')
elif opcao_escolida == 3 and opcao_comp == 'PAPEL':
    print('\nComputador escolheu', opcao_comp)
    print('Você escolheu TESOURA e o computador escolheu PAPEL, Computador GANHOU!')
else:
    print('OPÇÃO INVÁLIDA!!!')



