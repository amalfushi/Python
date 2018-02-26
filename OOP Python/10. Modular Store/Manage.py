import Store
import Product

class Manage(object):
    def __init__(self):
        self.stores = []
    
    def add_store(self, store):
        self.stores.append(store)
        return self

    def listAll(self):
        for store in self.stores:
            store.inventory()
    
if __name__ == "__main__":
    costco = Store.Store("Kirkland", "Franklin The Duck", "Costco")
    bestBuy = Store.Store("5th Level", "Satan", "BestBuy")

    falafel = Product.Product(3.5, "Falafel", 0.3, "The Best", 1.24)
    laptop = Product.Product(1000, "Aspire", .5, "Acer", 500)

    costco.add_product(falafel)
    bestBuy.add_product(laptop)

    myManager = Manage()
    myManager.add_store(costco).add_store(bestBuy).listAll()