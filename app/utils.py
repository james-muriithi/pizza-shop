def get_toppings():
    return [
        Toppings(name ="Mushrooms",price= 50 ),
        Toppings(name ="Cheese",price= 60 ),
        Toppings(name ="Broccoli",price= 80 )
    ]


class Toppings:
    toppings = []
    def __init__(self, name, price):
        self.price = price
        self.name = name  
        self.slug = name.replace(" ", "-").lower() 

    @classmethod
    def generate_toppings(cls):
        cls.toppings = [
            Toppings(name ="Mushrooms",price= 50 ),
            Toppings(name ="Cheese",price= 60 ),
            Toppings(name ="Broccoli",price= 80 )
        ]

    @classmethod
    def get_toppings(cls):
        cls.generate_toppings()
        return cls.toppings

    @classmethod
    def get_topping(cls, slug):
        return [topping for topping in cls.toppings if topping.slug == slug][0]

    def __repr__(self):
        return f"Topping {self.name}"