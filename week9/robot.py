class Robot:     #Creating robot class.
    MAX_ENERGY = 100    #Attritbute of energy.
    def __init__ (self):     #Initialising the functions of robot.
        self.name="Robot"   #Name
        self.age =  0       #Age
        self.energy = 0     #Energy

    def display(self):       #Display self, and all that is contained in self.
        print(f"I am {self.name}.")       #Printing I am - whatever is in self.name.
    def __repr__ (self):
        return f'robot(name={self.name}, age={self.age})'
    def __str__ (self):
        return f'Robot({self.name}, is {self.age} years old.'

if __name__ == "__main__":    #Testing class.
    robot = Robot()     #Calling the class.
    #robot.display()     #Displaying class.
    print(robot)

