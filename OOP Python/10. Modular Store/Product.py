class Product(object):
    def __init__(self, price, name, weight, brand, cost, status = "for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax = .105): #returns the price + tax.
        self.price += self.price * tax
        return self.price

    def returnProduct(self, reason): #changes some things based on reason for return
        self.return_reason = reason
        if self.return_reason == "defective":
            self.status = "defective"
            self.price = 0
        elif self.return_reason == "in the box, like new":
            self.status = "for sale"
        elif self.return_reason == "box opened":
            self.status = "used"
            self.price -= self.price * .2
        return self

    def displayInfo(self):
        print "Price: $", self.price
        print "Name: ", self.name
        print "Weight: ", self.weight, "lbs"
        print "Brand: ", self.brand
        print "Cost: $", self.cost
        print "Status: ", self.status
        print ""
        return self

if __name__ == "__main__":
    tacoSalad = Product(30, "Giant Taco Salad", 8, "Taco Bell", 10)
    laptop = Product(899, "Laptop", 3, "Acer", 700)
    elderSign = Product(9, "Elder Sign", 4.6, "Necronomicon Invocations", 900)

    tacoSalad.returnProduct("box opened")
    laptop.returnProduct("defective")
    elderSign.returnProduct("in box, like new")