n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
if n1 > n2 and n1 > n3:
    print(f'O número maior é: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O número maior é: {n2}')
else:
    print(f'O número maior é: {n3}')
if n1 < n2 and n1 < n3:
    print(f'O número menor é: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O número menor é: {n2}')
else:
    print(f'O número menor é: {n3}')
