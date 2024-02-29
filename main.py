from My_Objects import Category
from My_Objects import Product
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
        Category_prod = Category(item['name'], item['description'])
        for item2 in item['products']:
            # Создаем объект продукт
            Product_prod = Product(item2['name'], item2['description'], item2['price'], item2['quantity'])
            Products.append(Product_prod)
            # Добавляем продукт в список продуктов
            Category_prod.add_product(Product_prod)
            # Счетчик продуктов
            Category_prod.product_conter()
        Shop_category.append(Category_prod)

    new_product = Product.add_product('Xiaomi Redmi Note 11', '256GB, Серый цвет, 200MP камера', 35200, 350)
    # Работа gettera Product
    print(f'{new_product.price} руб.')
    # Работа сетера Product
    new_product.price = -10

    # Добавление продукта в список продуктов
    for item in Shop_category:
        product_list = item.products
        for item_2 in product_list:
            if item_2['name'] == new_product.name:
                item.add_product(new_product)

    # Распечатка цен на товары
    for item in Shop_category:
        #Работа Gettera Category
        print(item.price_list)

i = 0
