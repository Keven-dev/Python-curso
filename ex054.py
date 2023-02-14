from time import localtime
maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    anos = localtime()
    idade = anos[0] - ano_nasc
    if idade < 21:
        menor_idade += 1
    else:
        maior_idade += 1 
print(f'{menor_idade} pessoas são menores de idade e {maior_idade} pessoas são maiores de idade.')
