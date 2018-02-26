# class Hamburger(object):
#     def __init__(self, pattie_type = "Beef", bread_type = "Seasame-Seed Bun", cheese_type = "Sharp Cheddar"):
#         self.pattie_type = pattie_type
#         self.bread_type = bread_type
#         self.cheese_type = cheese_type

#     def display(self):
#         print "{} pattie with {} on a {}".format(self.pattie_type, self.cheese_type, self.bread_type)

# h1 = Hamburger()
# h2 = Hamburger("Bison and Chuck", "Kaiser Roll", "Smoked Gouda")
# h1.display()
# h2.display()

# #Classes are 'blueprints' from which objects are constructed.  Objects are instances of those blueprints

class Turtle(object):
    def __init__(self, skin_color, has_shell = True):
        self.skin_color = skin_color
        self.has_shell = has_shell
    def display():
        print self.skin_color, "\n", self.has_shell

class Ninja(Turtle):
    def __init__(self, skin_color, has_shell, weapon, color):
        super(Ninja, self).__init__(skin_color, has_shell)
        self.weapon = weapon
        self.color = color

n1 = Ninja("green", True, "sword", "red")