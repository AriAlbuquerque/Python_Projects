#Programa para calcular o dobro, o triplo e a RAIZ QUADRADA.
n = int(input('Digite um numero:'))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} é {}.'.format(n, d))
print('O triplo de {} é {}.'.format(n, t))
print('A raiz quadrada de {} é {:.2f}.'.format(n, r))

#/////////////////////////////////////////////////////////////////////////////////////////

n =int(input('Digite um numero:'))
print('O dobro de {} vale {},\nO trilplo de {} vale {}.\nA raiz quadrada de {} é: {:.2f}.'.format(n, (n*2), n, (n*3), n, (n**(1/2))))

#pow(n,(1/2)>>>>calcula raiz quadrada assim com o n**(1/2)