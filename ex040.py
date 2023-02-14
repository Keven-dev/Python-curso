print('='*33)
print('------------- SIEPE -------------')
print('='*33)
print(' ')

nota1 = float(input('Digite nota da 1º unidade: '))
nota2 = float(input('Digite nota da 2º unidade: '))
nota3 = float(input('Digite nota da 3º unidade: '))
nota4 = float(input('Digite nota da 4º unidade: '))
media = (nota1+nota2+nota3+nota4)/4
print(f'Média = {media}')
if media < 5:
    print('Situação do aluno: reprovado')
elif (media > 5) and (media < 7):
    print('Situação do aluno: Recuperação')
elif media >= 7:
    print('Situação do aluno: aprovado')
