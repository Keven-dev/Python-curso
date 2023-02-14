from random import randint
resposta = int(input('Tente adivinhar um número que eu pensei de 0 a 10: '))
tentativas = 1
n_aleatório = randint(0, 10)
while resposta != n_aleatório:
    resposta = int(input('Tente novamente de 0 a 10: '))
    tentativas += 1
print(f'Você acertou, com {tentativas} tentativa(s)')
