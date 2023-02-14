número = int(input('Digite um número: '))
multiplicador = número
multiplicando = número - 1
fatorial = resultado = 0
if número >= 2:
    while multiplicando != 0:
        resultado = (multiplicador * multiplicando)
        print(f'{multiplicador} x {multiplicando} = {resultado}')
        multiplicador = resultado
        multiplicando -= 1
        fatorial = resultado
    print(f'O fatorial de {número} é igual a {fatorial}')
elif número == 0 or número == 1:
    fatorial = 1
    print(f'O fatorial de {número} é igual a {fatorial}')
else:
    print(f'Não existe o fatorias de {número}, tente novamente.')