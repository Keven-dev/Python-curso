primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = primeiro + (10 - 1) * razão
for pa in range(primeiro, décimo, razão):
    print('{}'.format(pa), end=', ')
print('ACABOU')
