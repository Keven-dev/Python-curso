from random import randint

print('-='*25)
print(' VAMOS JOGAR IMPA OU PAR')

partidas_ganhas = 0
while True:
    print('-='*25)
    valor_jogador = int(input('Digite um valor inteiro: '))
    impa_par = str(input('Você esclhe INPAR ou PAR [I / P]?: ')).upper()
    print('-'*25)
    valor_comput = randint(0,10)
    soma = valor_jogador + valor_comput
    resultado = soma % 2
    if (impa_par == 'P'):
        if (resultado == 0): # verifica se o jogador acertou par
            partidas_ganhas += 1
            print(f'VOCÊ JOGOU {valor_jogador} E O COMPUTADOR {valor_comput}. TOTALIZANDO {soma} DEU PAR')
            print('-'*25)
            print('VOCÊ VENCEU!')
            print('VAMOS JOGAR NOVAMENTE...')
            print('-'*25)
        else:
            print(f'VOCÊ JOGOU {valor_jogador} E O COMPUTADOR {valor_comput}. TOTALIZANDO {soma} DEU IMPAR')
            print('-'*25)
            print('VOCÊ PERDEU!')
            break
    if (impa_par == 'I'):
        if (resultado != 0): # verifica se o jogador acertou impar
            partidas_ganhas += 1
            print(f'VOCÊ JOGOU {valor_jogador} E O COMPUTADOR {valor_comput}. TOTALIZANDO {soma} DEU IMPAR')
            print('-'*25)
            print('VOCÊ VENCEU!')
            print('VAMOS JOGAR NOVAMENTE...')
            print('-'*25)
        else:
            print(f'VOCÊ JOGOU {valor_jogador} E O COMPUTADOR {valor_comput}. TOTALIZANDO {soma} DEU par')
            print('-'*25)
            print('VOCÊ PERDEU!')
            break

print('-='*25)
print(f'GAME OVER! Você venceu {partidas_ganhas} vez(es)')