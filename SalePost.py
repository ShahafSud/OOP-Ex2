from Post import Post

class SalePost(Post):
    def __init__(self, owner, product, price, place):
        super().__init__(owner)
        self.__issold = False
        self.__product = product
        self.__price = price
        self.__place = place
        print(self)

    def sold(self, password):
        if (not self._owner.validat_pass(password)):
            return
        self.__issold = True
        print(self._owner.UN+"'s product is sold")

    def discount (self, precent, password):
        self._owner.validat_pass(password)
        if (precent >= 100):
            self.__price = 0
        self.__price -= (precent*self.__price)/100
        print("Discount on " + self._owner.UN + " product! the new price is: " + str(self.__price))

    def __str__(self):
        if self.__issold:
            sold_str = "Sold! "
        else:
            sold_str = "For sale! "
        return self._owner.UN + " posted a product for sale:\n" + sold_str + self.__product + ", price: " + str(self.__price) + ", pickup from: " + self.__place + "\n"




