média_idade = 0
nome_homen_velho = ''
idade_homen_velho = 0
qtd_mulher_nova = 0
for c in range(1, 5):
    print(f'=== Dados da {c}º pessoa ===')
    nome = str(input(f'Digite nome: ')).upper().strip()
    idade = int(input('Digite idade: '))
    sexo = str(input('Digite sexo (M ou F): ')).upper().strip()
    média_idade += idade
    if sexo == 'M' and idade > idade_homen_velho:
        nome_homen_velho = nome
    if sexo == 'F' and idade < 20:
        qtd_mulher_nova += 1
print('Média de idade do grupo: {:.0f} anos'.format(média_idade // 4))
print(f'Nome do homen mais velho: {nome_homen_velho}')
print(f'Quantidade de mulheres com menos de 20 anos: {qtd_mulher_nova}')
