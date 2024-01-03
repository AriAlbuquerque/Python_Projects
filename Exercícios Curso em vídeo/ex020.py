'''import math
ângulo = float(input('Digite o ângulo que desejar:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO {:.2f}.'.format(ângulo, seno))
coseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO {:.2f}'.format(ângulo, coseno))
tangente = math.tan(math.radians(ângulo))
print('o ângulo tem a TANGENTE {}.'.format(ângulo, tangente))'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que desejar:'))
seno = sin((radians(angulo)))
print('O ângulo {}, tem como SENO {:.2f}'.format(angulo, seno))
coseno = cos((radians(angulo)))
print('O ângulo {} tem como Cosseno {:.2f}'.format(angulo, coseno))
tangente = tan((radians(angulo)))
print('O ângulo tem como TANGENTE: {:.2f}'.format(angulo, tangente))
