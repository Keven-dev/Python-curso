n = int(input('Digite um número inteiro: '))
divisível = 0
for c in range(1, n+1):
    if n % c == 0:
        divisível += 1 
if divisível == 2:
    print(f'{n} é primo')   
else:
    print(f'{n} não é primo')
