print('='*31)
print('=== ANALISADOR DE TRIÂGULOS ===')
print('='*31)
reta1 = float(input('Digite o comprimento de uma reta: '))
reta2 = float(input('Digite de outra comprimento de uma reta: '))
reta3 = float(input('Digite de outra comprimento de uma reta: '))
if reta1 + reta2 < reta3:
    print('Os três segmentos de reta não podem formar um triângulo')
elif reta2 + reta3 < reta1:
    print('Os três segmentos de reta não podem formar um triângulo')
elif reta3 + reta1 < reta2:
    print('Os três segmentos de reta não podem formar um triângulo')
else:
    print('Os três segmentos de reta podem formar um triângulo')
