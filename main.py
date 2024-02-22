from My_Objects import Category
from My_Objects import Product
from My_func import load_json_from_file, counter_category, counter_product

if __name__ == '__main__':
    # Пример создания объекта
    category_1 = Category("Карандаши", "Канцтовары", 10, 2)
    Product_1 = Product("Карандаш простой", "Канцтовары", 35.43, 523, "Карандаши")

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
        Shop_category.append(Category_prod)
        for item2 in item['products']:
            Product_prod = Product(item2['name'], item2['description'], item2['price'], item2['quantity'], item['name'])
            Products.append(Product_prod)
    # Расчет количества категорий
    Category_cont = counter_category(Shop_category)
    # Расчет количества продуктов
    Product_cont_list = counter_product(Products)
    # Запись количества категорий в объект категория
    for item in Shop_category:
        item.category_count = Category_cont
    # Поиск и запись количества продуктов в объект категория
    for item in Shop_category:
        summ_prod = 0
        for item2 in Products:
            if item2.category_name == item.name:
                summ_prod += item2.quantity
        item.product_count = summ_prod
    i = 0
