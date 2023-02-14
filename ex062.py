primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro_termo
n_termos = 0
total_termos = 10
while n_termos < total_termos:
    print('{}, '.format(termo), end='')
    termo += razão
    n_termos += 1
    if n_termos == total_termos:
        print('PAUSA')
        novos_termos = int(input('Quantos termos a mais você deseja?: '))
        total_termos += novos_termos
print(f'Progressão finalizada com {total_termos} termos mostrados.')
