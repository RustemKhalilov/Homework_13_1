class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = Category.product_count + len(products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        summ = 0
        for item in self.__products:
            summ = summ + item['quantity']
        return summ

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
            self.__products.append(
                {'name': product_in.name, 'quantity': product_in.quantity, 'price': product_in.price})
            Category.product_count += len(self.__products)

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

    def __str__(self):
        return f'{self.name}, {self.price}. руб. Остаток: {self.quantity} шт.'

    def __add__(self, two_obj):
        return self.quantity * self.price + two_obj.quantity * two_obj.price

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


class ProductIterator:
    def __init__(self, In_categ: Category):
        self.In_categ = In_categ

    def __iter__(self):
        self.current_value = - 1
        return self

    def __next__(self):
        if self.current_value + 1 <= len(self.In_categ.get_products_list()) - 1:
           self.current_value = self.current_value + 1
           dict = self.In_categ.get_products_list()[self.current_value]
           return f"{dict['name']}, Цена {dict['price']} руб., Остаток {dict['quantity']} шт."
        else:
            raise StopIteration


