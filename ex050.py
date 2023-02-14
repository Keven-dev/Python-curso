soma_par = 0
n_par = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma_par += n
        n_par += 1
    else:
        pass
print(f'Existem {n_par} números pares e a soma deles é {soma_par}') 
