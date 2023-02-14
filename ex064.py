n = soma = qtd_números = 0
while n != 999:
    n = int(input('Digite um númro inteiro: '))
    if n != 999:
        soma += n
        qtd_números += 1
print(f'Foram digitados {qtd_números} números, e a soma é {soma}')
