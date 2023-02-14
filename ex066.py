valores_dig = soma = 0
while True:
    valor = float(input('Digite um valor (999 para):'))
    if valor == 999:
        break
    else:
        valores_dig += 1
        soma += valor
print(f'Foram digitados {valores_dig:.0f} valores, e soma entre eles é {soma:.0f}')
