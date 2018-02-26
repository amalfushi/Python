class Bike(object):
    def __init__(self, price=500, max_speed=25, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayinfo(self):
        print "Price--${}  |  Max Speed--{}mph  |  Miles--({})".format(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        self.miles += 10
        print "Riding"
        return self
    
    def reverse(self):
        print "Reversing"
        if self.miles-5 < 0:
            self.miles = 0
        elif self.miles >= 5:
            self.miles -=5
        return self

bike1 = Bike(1000, 30, 500)
bike2 = Bike(50, 20, 8763)
bike3 = Bike()

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()