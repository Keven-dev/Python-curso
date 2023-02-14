from time import localtime

atleta_nasceu = int(input('Digte ano de nascimento do atleta: '))
idade_atleta = localtime()
idade_atleta = idade_atleta[0] - atleta_nasceu

if idade_atleta > 0 and idade_atleta <= 9:
    print('Categoria: MIRIM')
elif idade_atleta > 0 and idade_atleta <= 14:
    print('Categoria: INFANTIL')
elif idade_atleta > 0 and idade_atleta <= 19:
    print('Categoria: JUNIOR')
elif idade_atleta > 0 and idade_atleta <= 20:
    print('Categoria: SÊNIOR')
elif idade_atleta > 20:
    print('Categoria: MASTER')
else:
    print('Categoria: NÃO DISPONIVEL')

