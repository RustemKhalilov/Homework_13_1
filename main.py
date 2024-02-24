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
        Product_list = []
        for item2 in item['products']:
            # Формируем словарь продуктов
            Product_list.append({item2['name']: item2['quantity']})
            # Создаем объект продукт
            Product_prod = Product(item2['name'], item2['description'], item2['price'], item2['quantity'])
            Products.append(Product_prod)
        # Создаем список объектов Product
        Category_prod = Category(item['name'], item['description'], Product_list)
        Shop_category.append(Category_prod)
