class Item:
    def Calcualte_total_price(self, x, y):            #self means python passes an object evertime a method is created inside a class
        return x*y
        
        
item1=Item()
item1.name= 'Livingston'
item1.price = 2000
item1.quality = 50
print(item1.Calcualte_total_price(item1.price, item1.quality))

item12=Item()
item12.name= 'Kongnyuy'
item12.price = 2500
item12.quality = 45
print(item12.Calcualte_total_price(item12.price, item12.quality))