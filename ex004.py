x = input('Digite algo: ')
print(type(x))
print('É numérico?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É decimal?', x.isdecimal())
print('É número e/ou letra?', x.isalnum())
print('Só tem espaços?', x.isspace())
print('Está em maiuscula?', x.isupper())
print('Está em menúscula?', x.islower())
print('Está captalizada?', x.istitle())
