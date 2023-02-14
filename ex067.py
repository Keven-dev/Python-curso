while True:
    valor = int(input('Deseja ver a tabuada de qual número? : '))
    print('='*20)
    if valor < 0:
        break
    else:
        for c in range(1, 11):
            resultado = valor * c
            print(f'{valor} x {c} = {resultado}')
    print('='*20)
print('===== TABUADA ENCERRADA =====')
 