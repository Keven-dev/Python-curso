diaalug = int(input('Quantos dias alugados?: '))
kmrodados = float(input('Quantos Km rodados?: '))
preco = (diaalug * 60) + (kmrodados * 0.15)
print('Valor a ser pago R${:.2f}'.format(preco))
