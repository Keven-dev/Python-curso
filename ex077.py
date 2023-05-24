palavras = ('estuadar', 'aprender', 'praticar', 'aplicar', 'refazer', 'corrigir', 'replicar', 'validar', 'autenticar', 'pensar', 'agir', 'focar', 'alcançar', 'conquistar', 'realizar')
vogal = ('a','e','i','o','u')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')





