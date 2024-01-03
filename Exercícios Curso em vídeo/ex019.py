'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjascente:'))
hi = (co ** 2 + ca ** 2 ) ** (1/2)

print('A hipotenusa vai medir:{:.2f}'.format(hi))'''

'''import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjascente:'))
hi = math.hypot(co, ca)

print(' A hipotenusa vai medir: {:.2f}'.format(hi))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjascente:'))
hi = hypot (co, ca)
print('O Valor da hipotenusa é: {:.2f}'.format(hi))
