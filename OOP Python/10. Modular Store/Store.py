class Store(object):
    def __init__(self, location, owner, name):
        self.products = []
        self.location = location
        self.owner = owner
        self.name = name
    
    def add_product(self, Product):
        self.products.append(Product)
        return self

    def remove_product(self, pName):
        for prod in self.products:
            if prod == pName:
                self.products.remove(prod)
        return self
    
    def inventory(self): #prints info on each product in products list
        print self.name, " inventory"
        for prod in self.products:
            prod.displayInfo()
        return self

if __name__ == "__main__":
    Mox_Boarding_House = Store("Arkham", "Madame Mox", "Mox Boarding House")
    Ikea = Store("Tukwila", "Swedish Prime Minister", "Ikea")