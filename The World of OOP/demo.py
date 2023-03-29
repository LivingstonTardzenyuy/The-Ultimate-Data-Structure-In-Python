
import csv

class Shop:
    pay_rate = 0.8          #a class attribute declaring the payrate
    all=[]    
    def __init__(self, name: str, price: int, quantity =0):
        
        
        #validation 
        assert price >=0, f"Price {price} The price must be greater than zero"
        assert quantity >=0, f"The quantity {quantity} must be greater than zero"
        
        self.name =name
        self.quantity = quantity
        self.price = price
        # print("All the itemts in the shop")
        
        #   actions to execute
        Shop.all.append(self)       #helps to append all the intances once created
        
    def calculate_quantity(self):
        return self.price * self.quantity
    
    def discount(self):
        self.price = self.price * self.pay_rate

    @classmethod        #using decorators
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            print (item)
        
    
    def __repr__(self):         #to represent the string representaion of an object
        return f"Shop('{self.name}', '{self.quantity}', '{self.price}')"
  
  
  
Shop.instantiate_from_csv()
    
# shop1 = Shop("Tk1", 100, 2)
# shop2 = Shop("Tk2", 200, 2)
# shop3 = Shop("Tk3", 500, 4)
# shop4 = Shop("Tk4", 700, 1)
# shop5 = Shop("Tk5", 90, 8)

# print(Shop.all)


# for instance in Shop.all:
    # print (instance.name)