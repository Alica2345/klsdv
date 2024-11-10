class Product:
    def __init__(self):
        self.name = "Alice"
        self.price = 14
        self.hight = 166

    def description(self):
        print(self.name, self.price, self.hight)


product1 = Product
product1.description()