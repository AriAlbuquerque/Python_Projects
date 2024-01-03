#Calculo de desconto e porcentagem.
preço = float(input('Digite o valor do produto:'))
novo = preço - (preço*5/100)
print('O produto custa R${}, com desconto de 5% custa:R$ {}.'.format(preço, novo))

preço = float(input('Qual é o preço do produto?'))
novo = preço - (preço * 5 / 100) #O preço do poduto - a porcentagem do desconto. preço-(preço*5/100)
print('O produto de valor {}, com desconto de 5% fica: {}. '.format(preço, novo))