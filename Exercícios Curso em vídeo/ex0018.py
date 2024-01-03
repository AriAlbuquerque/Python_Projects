'''import math
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num) ))

num = float(input('Digite um valor:'))
print('O valor digitado foi: {} e sua porção inteira é: {}'.format(num, int(num)))'''

from math import trunc
num = float(input('Digite um valor:'))
print('O valor digitado é: {} e sua parte inteira é {}'.format(num, trunc(num)))

