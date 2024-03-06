from My_Objects import Category
from My_Objects import Product
from My_Objects import ProductSmartphone
from My_Objects import ProductGrass
from My_Objects import noProduct
from My_Objects import ProductIterator
from My_func import load_json_from_file

if __name__ == '__main__':
    # Чтение данных из json
    path1 = "operations"
    file_name = "products.json"
    # Считали файл json
    dictionary_data = load_json_from_file(path1, file_name)
    # Создаем список из объектов и заполняем параметры для объекта
    Shop_category = []
    Products = []
    for item in dictionary_data:
        product_list = []
        for item2 in item['products']:
            # Создаем объект продукт
            Product_prod = Product(item2['name'], item2['description'], item2['price'], item2['quantity'], 'nocolor')
            # Проверка метода str
            print(f'Проверка метода Str для Product {Product_prod}')
            product_list.append({'name': item2['name'], 'quantity': item2['quantity'], 'price': item2['price']})
            Products.append(Product_prod)
        # Создаем категорию продукты
        Category_prod = Category(item['name'], item['description'], product_list)
        # Проверка метода str
        print(f'Проверка метода Str для Category {Category_prod}')
        # Счетчик продуктов
        # Category_prod.product_conter()
        Shop_category.append(Category_prod)

    new_product = Product.add_product('Xiaomi Redmi Note 11', '256GB, Серый цвет, 200MP камера', 35200, 350, 'nocolor')
    # Работа gettera Product
    print(f'{new_product.price} руб.')
    # Работа сетера Product
    new_product.price = -10

    # Добавление продукта в список продуктов
    for item in Shop_category:
        product_list = item.get_products_list()
        for item_2 in product_list:
            if item_2['name'] == new_product.name:
                item.add_product(new_product)

    # Распечатка цен на товары
    for item in Shop_category:
        # Работа Gettera Category
        print(item.products)

    # Работа метода str
    for item in Shop_category:
        # Работа Gettera Category
        print(item)

    Product_temp = Products[0] + Products[1]
    print('Работа метода add Product')
    print(Product_temp)
    # Работа итератора
    print('Работа итератора')
    Prod_iter = ProductIterator(Shop_category[0])
    for item in Prod_iter:
        print(item)

    Smartfon_1 = ProductSmartphone('Xiaomi Redmi Note 12', '256GB, Серый цвет, 200MP камера',
                                   42200, 150, 'черный', 1.8, 'Xiaomi Redmi Note 12', 256)

    Smartfon_2 = ProductSmartphone('Xiaomi Redmi Note 13', '512GB, Серый цвет, 200MP камера',
                                   65200, 100, 'белый', 2.2, 'Xiaomi Redmi Note 13', 512)

    Grass_1 = ProductGrass('Сельдерей', 'Двухлетняя овощная культура', 23, 352, 'зеленый', 'Россия', 3)
    Grass_2 = ProductGrass('Петрушка', 'Вид цветковых растений', 35, 150, 'зеленый', 'Россия', 3)

    print(f'Результат сложения одинаковых товаров = {Smartfon_1 + Smartfon_2}')
    print(f'Результат сложения разных товаров = {Smartfon_1 + Grass_1}')
    # Реализация проверки класса Product при добавлении в категорию
    TempProduct = noProduct
    Shop_category[0].add_product(TempProduct)
    # Реализация складывания продуктов
    print(Products[0] + Products[2])
    # Проверка пренадлежности к классу
    print(Products[0] + TempProduct)

i = 0  # Точка останова для отладки
