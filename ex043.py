peso = float(input('Digite peso ex:78.50 : '))
altura = float(input('Digite altura ex:1.80 : '))
imc = peso / altura**2

if imc < 18.5:
    print('Abaixo do peso')
elif imc >=18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25 and imc <= 30:
    print('Sobre peso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
print('IMC = {:.2f}'.format(imc))
