#Programa para conversão de moedas.

real = float(input('Quanto voce tem em real? R$'))
dolar = real/ 3.27
print('Com R$ {:.2f} você comprará: {:.2f} US$.'.format(real, dolar))
