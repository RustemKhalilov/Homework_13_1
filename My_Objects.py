class Category:
    category_count = 0
    product_count = 0
    product_list = []

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = None
        Category.category_count += 1
        Category.product_list.append(name)

    def product_conter(self):
        """
        Метод для вычисления количества продуктов из приватного списка продуктов
        """
        Category.product_count += len(self.__products)

    def add_list_product(self, product_list):
        """
        Метод для добавления списка продуктов в приватное свойство __products
        """
        self.__products = product_list

    @property
    def get_list_product(self):
        """
        Метод для добавления списка продуктов в приватное свойство __products
        """
        return self.__products


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def price_list(self):
        return f'{self.name}, {self.price} руб. Остаток {self.quantity} шт.'

    @classmethod
    def add_product(cls, name: str, description: str, price: float, quantity: float):
        return cls(name, description, price, quantity)

    def add_new_product(self, new_product):
        """
       Метод принимает на вход товар и проверяет на совпадение
        """
        # Если имена совпадают то мы складываем товары по количеству
        if new_product.name == self.name:
            self.quantity = self.quantity + new_product.quantity
            if self.price < new_product.price:
                self.price = new_product.price
            return True
        else:
            return False

    @property
    def price_info(self):
        if self.price <= 0:
            print("Цена не корректная")
        else:
            print(f'{self.price} руб.')
            return self.price


    @price_info.setter
    def price_correct(self, new_price):
        self.price = new_price
