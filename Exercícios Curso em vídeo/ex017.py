#Programa para aluguel de carros.
dias = int(input('Quantos dias alugado?'))
km = float(input('Quantyos Km rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}.'.format(pago))


dias = int(input('Quantos dias alugados:'))
km = float(input('Quantos Km rodados?'))
