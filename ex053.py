frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'Temos um palindromo {junto} é {inverso}') 
else:
    print(f'{junto} e {inverso} não é palindromo')
