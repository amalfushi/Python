class Pet(object):
    def __init__(self, name, age, fur):
        self.name = name
        self.age = age
        self.fur = fur
        self.legs = 4

    def speak(self):
        print 'uhhhhhhhhhhhhhhh'
        return self

    def printPet(self):
        print self.name, " - ", self.age, " - ", self.fur, " - ", self.legs
        return self

    def move(self):
        print "I'm moving"
        print "I'm done moving"
        return self

pet1 = Pet('Frankie', 5, 'gold')
pet2 = Pet('Barnaby Jones', 7, 'tabby')
pet3 = Pet('Tina', 12, 'wool')

pets = [pet1,  pet2, pet3]

for pet in pets:
    pet.printPet()

pet1.printPet().speak().move().move().speak()
pet1.legs = 3
pet1.printPet()