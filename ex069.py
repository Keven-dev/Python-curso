sexo = continua = ''
maior_idade = h_cad = m_menos20 = 0


while True:
    print('-'*30)
    idade = int(input('Digite idade: '))
    if idade > 18:
        maior_idade += 1   
    while (sexo != 'M') or (sexo != 'F'):
        sexo = str(input('Digite o sexo [M / F]: ')).upper()
        if sexo == 'M':
            print('Homen')
            h_cad += 1
            break
        elif sexo == 'F':
            print('Mulher')      
            if idade < 20:
                m_menos20 += 1
            break        
    print('-'*30)            
    continua = str(input('Deseja continuar? [S / N]: ')).upper()
    if continua == 'S':
        pass
    elif continua == 'N':
        break
    
print('='*30)
print('FIM DO PROGRAMA')
print('='*30)
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {h_cad} homen(s) cadastrado(s)')
print(f'E temos {m_menos20} mulher(es) com menos de 20 anos')
