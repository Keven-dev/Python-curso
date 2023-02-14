from time import localtime

print('==== ALISTAMENTO ====')
print(' ')
ano_nascimento = int(input('Digite ano de nascimento: '))
ano_atual = localtime()
ano_atual = ano_atual[0]
idade = ano_atual - ano_nascimento
if idade < 18:
    faltam_ano = 18 - idade
    print(f'Idade insificiente para alistamento, falta aproximadamente {faltam_ano} ano(s).')
elif idade == 18:
    print('É hora de se alistar.')
elif idade > 18:
    passou_ano = idade - 18
    print(f'Já passou da hora de se alistar, passou aproximadamente {passou_ano} ano(s) ')
else:
    print('Ouve algum erro, tente novamente!')
