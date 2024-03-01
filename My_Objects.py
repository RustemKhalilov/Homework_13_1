class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1

    def product_conter(self):
        """
        Метод для вычисления количества продуктов из приватного списка продуктов
        """
        Category.product_count += len(self.__products)

    def add_product(self, product_in):
        """
        Метод для добавления списка продуктов в приватное свойство __products
        """
        id_product = 0
        for item in self.__products:
            if item['name'] == product_in.name:
                item['quantity'] = item['quantity'] + product_in.quantity
                id_product = 1
        if id_product == 0:
            self.__products.append({'name': product_in.name, 'quantity': product_in.quantity, 'price': product_in.price})

    @property
    def products(self):
        """
        Метод выводит на печать остаток продуктов
        """
        result = ''
        for item in self.__products:
            result += f'{item["name"]}, {item["price"]} руб. Остаток {item["quantity"]} шт.\n'
        return result


    def get_products_list(self):
        """
        Метод возвращает список продуктов
        """
        return self.__products


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: float):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity



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
            if self.__price < new_product.price:
               self.__price = new_product.price
            return True
        else:
            return False

    @property
    def price(self):
        if self.__price <= 0:
            print("Цена не корректная")
        else:
            return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = new_price
