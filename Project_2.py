class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        new_product = Product(name, quantity)
        self.__products.append(new_product)

    def show_products(self):
        for product in self.__products:
            print(f"สินค้า: {product.name}, จำนวน: {product.quantity}")
my_store = Store()
my_store.add_product("Laptop", 15)
my_store.add_product("Mouse", 50)
my_store.show_products()
