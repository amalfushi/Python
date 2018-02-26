class Dog (object):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def speak(self, otherDog):
        print "{} barked at {}".format(self.name, otherDog.name)
        return self


ray = Dog("Ray", "Michael Choi")
frankie = Dog("Frankie", "Ray")

ray.speak(frankie).speak(frankie).speak(frankie)
frankie.speak(ray).speak(frankie)