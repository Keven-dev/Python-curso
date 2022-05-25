preço = float(input('Digite valor do produto R$:  '))
desc = preço - (preço * 5 / 100)
print('Produto de R${:.2f} com 5% de desconto ------ R${:.2f}'.format(preço, desc))
