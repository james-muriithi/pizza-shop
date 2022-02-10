def get_toppings():
    return [
        Toppings(name ="Mushrooms",price= 50 ),
        Toppings(name ="Cheese",price= 60 ),
        Toppings(name ="Broccoli",price= 80 )
    ]


class Toppings:
    def __init__(self, name, price):
        self.price = price
        self.name = name  
        self.slug = name.replace(" ", "-").lower() 