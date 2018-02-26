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

class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner
    
    def add_product(self, Product):
        self.products.append(Product)
        return self

    def remove_product(self, pName):
        for prod in self.products:
            if prod == pName:
                self.products.remove(prod)
        return self
    
    def inventory(self): #prints info on each product in products list
        for prod in self.products:
            prod.displayInfo()
        return self

p1 = Product(30, "Giant Taco Salad", 8, "Taco Bell", 10)
p2 = Product(899, "Laptop", 3, "Acer", 700)
p3 = Product(9, "Elder Sign", 4.6, "Necronomicon Invocations", 900)

p1.returnProduct("box opened")
p2.returnProduct("defective")
p3.returnProduct("in box, like new")

Mox_Boarding_House = Store("Arkham", "Madame Mox")
Mox_Boarding_House.add_product(p1).add_product(p2).add_product(p3)
Mox_Boarding_House.inventory()
Mox_Boarding_House.remove_product(p1)
Mox_Boarding_House.inventory()