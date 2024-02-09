from typing import override

from Post import Post

class SalePost(Post):
    def __init__(self, owner,sold,product, price, place, available):
        super().__init__(owner)
        self.sold = False
        self.product = product
        self.price = price
        self.place = place
        self.available = available
        print(self._owner.UN + "posted a product for sale:\n For sale! " + self.product + ", price: " + str(self.price) + ", pickup from: " + self.place)

    def sold(self):
        self.sold = True
        print(self._owner.UN+"'s product is sold")

    def discount (self, precent, password):
        self._owner.validat_pass(password)
        if (precent >= 100):
            self.price = 0
        self.price -= (precent*self.price)/100
        print("Discount on " + self._owner.UN + "product! the new price is: " + str(self.price))

    def print(self):
        print("sold! " + self.product + ", price: " + str(self.price) + ", pickup from: " + self.place)




