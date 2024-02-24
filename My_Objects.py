class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products, number_of_categories=-2115,
                 total_number_of_unique_products=-2116):
        self.name = name
        self.description = description
        self.number_of_categories = number_of_categories
        self.total_number_of_unique_product = total_number_of_unique_products
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    def __repr__(self):
        return f'{self.name} \n  {self.description} \n {self.number_of_categories} \n {self.total_number_of_unique_product}'


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.name} \n  {self.description} \n {self.price} \n {self.quantity}'
