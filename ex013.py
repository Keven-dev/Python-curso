salario = float(input('Digite salário do funcionário R$: '))
aumento = salario + (salario * 15 / 100)
print('Novo salário ajustado para mais 15% ---> R${:.2f}'.format(aumento))
