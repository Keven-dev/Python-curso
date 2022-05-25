vl = float(input('Digite a sua velocidade atual Km/h: '))
if vl > 80:
    vl_exed = vl - 80
    multa = vl_exed * 7
    print('Você excedeu {:.1f}Km/h, Multa de {:.2f}R$'.format(vl_exed, multa))
else:
    print('Tudo ok, você não foi multado.')
