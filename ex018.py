from math import radians, sin, cos, tan
ang = int(input('Digite valor do ângulo: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {:.0f}° tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {:.0f}° tem o COSSENO de {:.2f}'.format(ang, coss))
print('O ângulo de {:.0f}° tem a TANGENTE de {:.2f}'.format(ang, tang))
