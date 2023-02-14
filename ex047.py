n_inicial = int(input('Digite um número: '))
n_final = int(input('Digite outro maior que o primeiro número: '))
if n_inicial < n_final:
    print(f'Numeros pares de {n_inicial} a {n_final}!!')
    n_pares = 0
    for p in range(n_inicial, n_final+1):
        if p % 2 == 0:
            print(p)
            n_pares += 1
    print(f'\nNo intervalo de {n_inicial} a {n_final} existem {n_pares} números pares')
else:
    print(f'\nO segundo número escolhido tem que ser maior que o primeiro, você escolheu {n_inicial} e depois {n_final}, tente novamente!')
