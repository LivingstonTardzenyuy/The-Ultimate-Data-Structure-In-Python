class Store:
    def __init__(self, name: str, price: int, quantiy: int):
        self.discount = 0.8  # class attribute
        assert price >= 0, f"The price entered should be greater than zero"
        assert quantiy >= 0, f"the quantity entered should be greater than zero"

        self.name = name
        self.price = price
        self.quantity = quantiy

    def calculate_quantity(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.discount

price = 20000
quantiy = 5
name = "Kongnyuy"

stor = Store(name, price, quantiy)
# print(stor.calculate_quantity())
stor.apply_discount()
print(Store.__dict__)               #accessing all the attributes at the class level
# print(stor.__dict__)                   #accesing all the attributes at the instance level
# print(Store.discount)

print(stor.apply_discount())