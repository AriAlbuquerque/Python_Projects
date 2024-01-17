#Operadores Aritméticos:

print(5 + 3)       # Adição
print(5 - 3)       # Subtração
print(5 * 3)       # Multiplicação
print(5 / 3)       # Divisão
print(5 // 3)      # Divisão Inteira
print(5 % 3)       # Módulo (resto da divisão)

# Em Python as FUNÇÕES são blocos de código reutilizáveis que podem ser definidos usando a palavra-chave def.
# Podem ser chamados com o nome da função e os parâmetros devem ser fornecidos na chamada.

def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")


#  if...elif...else
#  Os comandos if, elif e else são usados para criar ramificações condicionais no fluxo do programa.
# Por exemplo:

x = 5
if x > 0:
    print("X é POSITIVO")
elif x < 0:
    print("X é NEGATIVO")
else:
    print("X é ZERO")

# While cria um loop que será executado enquanto a condição especificada for verdadeira.
# Por exemplo:
    
    x = 5
while x > 0:
    print(x)
    x -= 1

# For é usado para iterar sobre uma sequência, como uma lista ou uma string. 
# Por exemplo:
    
for i in range(6):
    print(i)

    