# Calcular área e quantidade de tinta usada para pintar uma parede.

larg = float(input('Qual a largura da parede:'))
alt = float(input('Qual a altura da parede:'))
área = larg * alt
tinta = área / 2
print('A dimensão da sua parede é {}m de altura x {}m de largura.\nSua área é de {:.2f}m2, \nvocê precisará de {} litros de tinta.'.format(larg, alt, área, tinta))

#larg = float(input('Largura da parede:'))
#alt = float(input('Digite a alltura da parede:'))
#area = larg * alt # A área é largura x altura.
#print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2'.format(larg, alt, area))
#tinta = area/2
#print('Para pintar essa parede você precdisa de {} litros de tinta.'.format(tinta))
