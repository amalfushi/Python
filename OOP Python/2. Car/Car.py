class Car(object):
    def __init__(self, price=0, speed=0, fuel=0, mileage=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price >= 10000:
            self.tax =.15
        else:
            self.tax = .12

    def display_all(self):
        print "Price: ", self.price
        print "Speed: ", self.speed, "mph"
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage, "mpg"
        print "Tax: ", self.tax
        print ""

car1 = Car(2000, 35, "Full", 15)
car2 = Car(2000, 5, "Not Full", 105)
car3 = Car(2000, 15, "Kind of Full", 95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 25)
car6 = Car(2000000, 35, "Empty", 15)

arrCar = [car1, car2, car3, car4, car5, car6]

for car in arrCar:
    car.display_all()