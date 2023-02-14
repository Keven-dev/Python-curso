sexo = ''
opção = 'S'
while opção == 'S':
    sexo = str(input('Dgite seu sexo [M / F]: ')).upper().strip()
    if (sexo != 'M') and (sexo != 'F'):
        print('Opção inexistente!') 
    opção = str(input('Deseja continuar? [S / N]:')).upper().strip()
