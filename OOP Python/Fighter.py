class Fighter(object):
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def hit(self, otherFighter):
        otherFighter.health -= self.attack
        print '{} attacked {} for {} damage'.format(self.name, otherFighter.name, self.attack)
        print '{} is at {} health'.format(otherFighter.name, otherFighter.health)
        return self

    def display(self):
        print self.name, " - ", self.health, " - ", self.attack

ray = Fighter('Ray', 100, 3)
mChoi = Fighter('Michael Choi', 600, 50)

ray.display()
mChoi.display()

ray.hit(ray).hitray)
ray.hit(mChoi)
mChoi.hit(ray).hit(ray)

