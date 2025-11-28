class Inhabitant:
    MAX_ENERGY = 100
    def __init__ (self, name, age, energy):
        self.name = "Inhabitant"
        self.age = 0
        self.energy = 100

    def __repr__(self):
        return f'Inhabitant(name={self.name}, age={self.age}, energy={self.energy})'
    def __str__(self):
        return f'Inhabitant({self.name} is {self.age} years old and has {self.energy} energy)'

