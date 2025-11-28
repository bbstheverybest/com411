from inhabitant import Inhabitant


class Robot(Inhabitant):     #Creating robot class.
    MAX_ENERGY = 100    #Attritbute of energy.
    def __init__ (self, name, age, energy): #Initialising the functions of robot.
       super().__init__(name, age, energy)
       self.laws = 10

    def display(self):       #Display self, and all that is contained in self.
        print(f"I am {self.name}.")       #Printing I am - whatever is in self.name.
    def __repr__ (self):
        return f'robot(name={self.name}, age={self.age})'
    def __str__ (self):
        return f'Robot({self.name}, is {self.age} years old, and has {self.energy} energy)'

if __name__ == "__main__":    #Testing class.
    robot = Robot()     #Calling the class.
    #robot.display()     #Displaying class.
    print(robot)

    robot.move(10)

