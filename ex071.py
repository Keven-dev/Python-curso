val = int(input('Digite o valor a ser sacado: '))
céd50 = céd20 = céd10 = céd01 = 0
if val >= 1:
    while True:
        if val >= 50:
            céd50 += 1
            val -= 50
    
        elif val >= 20:
            céd20 += 1
            val -= 20
    
        elif val >= 10:
            céd10 += 1
            val -= 10 
    
        elif val >= 1:
            céd01 += 1
            val -= 1
    
        if val == 0:
            break

    print(f'Cédulas de 50R$: {céd50}')
    print(f'Cédulas de 20R$: {céd20}')
    print(f'Cédulas de 10R$: {céd10}')
    print(f'Cédulal de R$01: {céd01}')
else:
    print('Impossível sacar esse valor!')
