primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro_termo
n_termos = 1
while n_termos <= 10:
    print('{}, '.format(termo), end='')
    termo += razão
    n_termos += 1
print('FIM')   
