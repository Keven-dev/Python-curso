sal = float(input('Digite seu salário R$: '))
if sal <= 1250:
    aumento = sal * 15 / 100
    sal = aumento + sal
else:
    aumento = sal * 10 / 100
    sal = aumento + sal
print("O aumento foi de {:.2f}R$ totalizando {:.2f}R$".format(aumento, sal))
