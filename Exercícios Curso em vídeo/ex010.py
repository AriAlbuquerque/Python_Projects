# Programa para Conversor de medidas.

medida = float(input('Digite o valor em metro:'))
cm = medida*100
mm = medida*1000
print('A medida em metros é:{}.\nEm centímetros é: {:.2f}.\nEm milimetros é: {:.2f}.'.format(medida, cm, mm))

