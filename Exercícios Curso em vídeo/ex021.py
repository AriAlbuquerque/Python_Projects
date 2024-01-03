import random
a1 = str(input('Digite um nome:'))
a2 = str(input('Digite outro nome:'))
a3 = str(input('Digite outro nome:'))
a4 = str(input('Digite o último nome:'))
lista = [a1, a2, a3, a4]
aluno = random.choice(lista)
print('O aluno escolhido foi: {}!'.format(aluno))