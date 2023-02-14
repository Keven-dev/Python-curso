tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um núnero entre 0 e 20: '))
if n >= 0 and n <= 20:
    print(f'Você digitou o número {tupla[n]}')
else:
    print('Tente novamente!')
