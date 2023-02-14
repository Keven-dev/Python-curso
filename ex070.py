print('-'*50)
print('                LOJA VARIEDADE')
print('-'*50)
total = prod_mil = prod_barat = n_prod_barat = c  = 0
opção = ''
while opção != 'N':
    n_produto = str(input('Digite nome do produto: '))
    
    preço = float(input(f'Digite o preço do/da {n_produto} R$: '))
    total += preço
    if c == 0:
        prod_barat = preço
        n_prod_barat = n_produto
    if c > 0:
        if preço < prod_barat:
            n_prod_barat = n_produto
            prod_barat = preço
    if preço > 1000:
        prod_mil += 1
    while opção != 'S' or opção != 'N':
        opção = str(input('Deseja continuar? [S/N]: ')).upper()
        if opção == 'S':
            break
        if opção == 'N':
            break
            
    c += 1
       
print('-'*10,'FIM DO PROGRAMA','-'*10)
print(f'Total das compras R$: {total}')
print(f'Temos {prod_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {n_prod_barat} que custa R${prod_barat}')
