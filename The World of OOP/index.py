
#basic data type

item1='phone'
item1_price= 100
item2_quality= 5
item1_price_total= item1_price * item2_quality

print(type(item1))
print(type(item1_price))
print(type(item2_quality))
print(type(item1_price_total))


#advance form

print("advance form")
class Item:
    # def __init__(self, price, quality)
    pass
    
item1=Item()        #creating an instance of a class
item1.name= 'phone'
item1.price = 500
item1.quality = 5

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quality))