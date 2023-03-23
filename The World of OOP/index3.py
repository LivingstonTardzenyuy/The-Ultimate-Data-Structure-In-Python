class Item:
    def __init__(self, name: str, quality: float, price=0):                 #help python to call the actions inside the init
        
        #run validations to recieved arguments
        assert price>=0, f"Price {price} is not greater than zero!"         #to make sure we recieve valid data
        assert quality>=0, f"quality {quality} is not greater than zero"
        
        
        print(f"An instance created for: {name}")
        self.name=name              #passing attriubes dynamically
        self.quality=quality
        self.price=price
        
        
        
    # for each method we design in our class the instance object in this case item12 is pass as an argument
    def calculate_total_price(self):            #by default the instance object is pass as an argument
        return self.price * self.quality
                
item2=Item("Livingston", "200", 5)
print(item2.calculate_total_price())