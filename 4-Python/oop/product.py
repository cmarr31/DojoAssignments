class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        self.price = self.price * (1 + tax)
        return self.price
    def return_item(self, reason):
        self.return_reason = reason
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "open box":
            self.status = "used"
            self.price = self.price * .8
        else:
            self.status = "for sale"
        return self
    def display_info(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        print "Return reason:", self.return_reason
p1 = Product(99.99,"Ugly Doll",10,"Mattel")
p1.add_tax(0.07)
p1.sell()
p1.return_item("open box")
p1.display_info()