class Vehicle(object):
    def __init__(self, color, typeOf, speed, noise):
        self.color = color
        self.typeOf = typeOf
        self.speed = speed
        self.noise = noise

    def honk(self):
        print self.noise
        return self

    def printVehicle(self):
        print self.typeOf, " - ", self.color, " - ", self.speed, " - ", self.noise
        return self

car = Vehicle("red", "Hyundai", 88, "beep beep")
bike = Vehicle("yellow", "Schwinn", 30, "brrrring briiinggg")

car.printVehicle().honk().honk()
bike.printVehicle().honk().honk()