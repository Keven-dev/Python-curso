from platform import processor


maior_p = 0
maior_p = 0
for c in range(1, 6):
    peso = float(input(f'Digite peso da {c}º pessoa Kg: '))
    if c == 1:
        menor_p = peso
        maior_p = peso
    else:
        if peso < menor_p:
            menor_p = peso
        if peso > maior_p:
            maior_p = peso
print('O menor peso lido foi {:.2f}Kg \nO maior peso lido foi {:.2f}Kg'.format(menor_p, maior_p))
