import os.path
import json
from My_Objects import Category
from My_Objects import Product

def load_json_from_file(path1, file_name):
    """
    Функция возвращает объект по строкам из json файла
    """
    file_ID = os.path.join(path1, file_name)  # Считываем файл с диска
    with open(file_ID, 'r', encoding='utf-8') as file_JS:  # Читаем файл построчно
        return json.load(file_JS)


def counter_category(list_category: list):
    """
    Возвращает количество категорий
    """
    category_list = []
    for item in list_category:
        category_list.append(item.name)
        my_set = set(category_list)
    return len(my_set)


def counter_product(list_product: list):
    """
    Возвращает количество продуктов
    """
    product_list = []
    for item in list_product:
        product_list.append(item.name)
        my_set = set(product_list)
    product_list_resume = list(my_set)
    product_list_dict = {}
    for item in product_list_resume:
        product_list_dict[item] = 0
    for item in list_product:
        product_list_dict[item.name] = product_list_dict[item.name] + item.quantity
    return product_list_dict


