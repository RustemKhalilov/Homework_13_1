class Category:
    def __init__(self, name: str, description: str, products: str, number_of_categories: int, total_number_of_unique_products: int):
        self.name = name
        self.description = description
        self.products = products
        self.number_of_categories = number_of_categories
        self.total_number_of_unique_product = total_number_of_unique_products


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
