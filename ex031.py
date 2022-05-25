distancia = float(input('Digite a distância de sua viagem em Km: '))
if distancia <= 200:
    vl_passagem = distancia * 0.50
    print('O valor calculado foi de {:.2f}R$'.format(vl_passagem))
else:
    vl_passagem = distancia * 0.45
    print('O valor calculado foi de {:.2f}R$'.format(vl_passagem))
