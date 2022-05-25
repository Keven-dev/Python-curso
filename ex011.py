alt = float(input('Digite a altura da parede em metro(s): '))
larg = float(input('Digite a largura da parede em metro(s): '))
ária = larg * alt
tinta = ária / 2
print('Para pintar a sua parede de {:.1f} m², será necessário {:.1f}/L  de tinta.'.format(ária, tinta))
