# Atributo de classe (compartilhado por todas as instâncias da classe)

class Animal:
    total_animals = 0

# Construtor da classe (inicializa o objeto)
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.total_animals += 1

 # Método da classe (comportamento do objeto)
        
    def sound(self):
        print("This animal makes a sound.")


# Criando objetos da classe Animal
        
animal1 = Animal("Bobby", "Dog")
animal2 = Animal("Whiskers", "Cat")

# Acessando atributos e métodos do objeto

print(animal1.name)
print(animal1.species)
animal1.sound()

# Acessando atributo de classe

print("Total number of animals:", Animal.total_animals)