from ast import Break


print('='*20,' PAGAMENTO ','='*20)
print(' ')
valor_mercadoria = float(input('Digite o valor da mercadoria R$: '))
print('\nCONDIÇÕES DE PAGAMENTO\n')
print('1 - À VISTA DINEIRO OU CHEQUE: 10% DE DESCONTO\n2 - À VISTA NO CARTÃO: 5% DE DESCONTO\n3 - EM ATÉ 2X NO CARTÃO: PREÇO NORMAL\n4 - 3X OU MAIS NO CARTÃO: 20% DE JUROS\n'  )
condicao_pag = int(input('Condição(1, 2, 3 ou 4): '))
condicaos = [1, 2, 3, 4]
desconto = 0
juros = 0
if condicao_pag == 1:
    desconto = desconto + (valor_mercadoria * 10 /100)
    valor_mercadoria = valor_mercadoria - desconto
elif condicao_pag == 2:
    desconto = desconto + (valor_mercadoria * 5 /100)
    valor_mercadoria = valor_mercadoria - desconto
elif condicao_pag == 3:
    valor_mercadoria = valor_mercadoria * 1 # Preço normal
elif condicao_pag == 4:
    juros = juros + (valor_mercadoria * 20 /100)
    valor_mercadoria = valor_mercadoria + juros
else:
    print('CONDIÇÃO INVÁLIDA')
    valor_mercadoria = 'ANULADO'
print('\nValor a ser pago R${:.2f}'.format(valor_mercadoria))
