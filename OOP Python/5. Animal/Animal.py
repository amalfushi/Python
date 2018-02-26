class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -=1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "The {} has {} remaining health".format(self.name, self.health)

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "My name is {}. I have {} remaining health".format(self.name, self.health)
        print "I am a Dragon"
    

dog = Dog("Kitty")
dog.walk().run().displayHealth()
dog.pet().pet().displayHealth()

falcor = Dragon("Falcor")
falcor.displayHealth()
falcor.fly().fly().fly().displayHealth()