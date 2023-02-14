print('==== COMPRA DE IMÓVEL ====')
print(' ')
valor_casa = float(input('Digite valor da casa: '))
sal_comprador = float(input('Digite o salário mensal do comprador: '))
ano = int(input('Digite o número de anos que o comprador deseja pagar a casa: '))

valor_mensal = valor_casa // (ano * 12)
sal_comprador = sal_comprador * 30 / 100

if valor_mensal > sal_comprador:
    print('Compra do imóvel NEGADO!')
    print(f'Mensalidade: R${valor_mensal}')
    print('Pagamento da casa exede 30% do salário do comprador.')
else:
    print('Compra realizada com sucesso!')
    print(f'Mensalidade: R${valor_mensal}')