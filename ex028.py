from pyfirmata import Arduino
from time import sleep
from random import randint

Uno = Arduino('COM6')
ledVerde = 6
ledVermelho = 3
buzzer = 10

while True:
    Uno.digital[ledVerde].write(0)
    Uno.digital[ledVermelho].write(0)
    n_escolhido = randint(0, 5)
    n_user = int(input('Tente adivinhar o número escolhido de 0 a 5: '))
    if n_user == n_escolhido:
        print('Você acertou, parabéns!')
        Uno.digital[buzzer].write(1)
        sleep(0.02)
        Uno.digital[buzzer].write(0)
        Uno.digital[ledVerde].write(1)
        sleep(0.5)
        break

    else:
        print('Você errou! era o número {}'.format(n_escolhido))
        Uno.digital[buzzer].write(1)
        sleep(0.02)
        Uno.digital[buzzer].write(0)
        Uno.digital[ledVermelho].write(1)
        sleep(0.5)
