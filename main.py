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
        Product_list = {}
        for item2 in item['products']:
            # Формируем словарь продуктов
            Product_list[item2['name']] = item2['quantity']
            # Создаем объект продукт
            Product_prod = Product(item2['name'], item2['description'], item2['price'], item2['quantity'])
            Products.append(Product_prod)
        # Создаем список объектов Product
        Category_prod = Category(item['name'], item['description'])
        #Счетчик продуктов
        Category_prod.product_conter()
        Category_prod.add_list_product(Product_list)
        Shop_category.append(Category_prod)
    for item in Products:
        print(item.price_list)
    new_product = Product.add_product('Xiaomi Redmi Note 11', '256GB, Серый цвет, 200MP камера', 35200, 350)

    id_product = 0
    for item in Products:
        if item.add_new_product(new_product) == True:
           id_product = 1
    if id_product == 0:
       Products.append(new_product)

    # Добавление продукта в список продуктов
    for item in Shop_category:
        product_list = item.get_list_product
        for key, value in item.get_list_product.items():
            if key == new_product.name:
               product_list[key] = value + new_product.quantity
            item.add_list_product(product_list)
    #Распечатка цен на товары
    for item in Products:
        print(item.price_list)
    #По идеи продукт может быть такой что его нет в категориях
    #Тогда нужно создать категорию, но в входных данных на продук нет сведения о категории


i= 0